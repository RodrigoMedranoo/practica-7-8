from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User 
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .form import ReservacionForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request,"home.html",{
        "msg":"Cibernetica de 4to semestre"
    })

def registro(request):
    if request.method == 'GET':
        return render(request,"registro.html",{
        "form": UserCreationForm
    })
    else:
        #aqui tenemos nuestro POST
        req = request.POST
        if req['password1'] == req['password2']:
            try:
                user = User.objects.create_user(
                    username=req['username'],
                    password=req['password2']
                )
                user.save()
                login(request,user)
                return redirect("/")
            except IntegrityError as ie:
                return render(request,"registro.html",{
        "form": UserCreationForm,
        "msg" : "Ese usuario ya existe"
    })
            except Exception as e:
                return render(request,"registro.html",{
        "form": UserCreationForm,
        "msg" : "Hubo un error {e}"
    })
        else:
            return render(request,"registro.html",{
        "form": UserCreationForm,
        "msg" : "Revisa que las contraseñas coincidan"
    })
        
def iniciarSesion(request):
    if request.method == "GET":
        return render(request,"login.html",{
            "form": AuthenticationForm,
    })
    else:
        try:
            user= authenticate(request,
                                username=request.POST['username'],password=request.POST['password'])
            if user is not None:
                    login(request, user)
                    return redirect("/")
            else: 
                    return render(request,"login.html",{
                    "form": AuthenticationForm,
                    "msg" : "El usuario o la contraseña son incorrectos "
            })
        except Exception as e:
                 return render(request,"login.html",{
                    "form": AuthenticationForm,
                    "msg" : "Hubo un error {e}"
            })
def cerrarsesion(request):
    logout(request)
    return redirect ("/")

@login_required
def nuevaReservacion(request):
      if request.method == "GET":
        return render(request,"nuevareservacion.html",{
                        "form": ReservacionForm
                })
      else:
           try:
                form = ReservacionForm(request.POST)
                if form.is_valid():
                        nuevo  = form.save(commit=False)
                        if request.user.is_authenticated:
                            nuevo.usuario=request.user
                            nuevo.save()
                            return redirect("/")
                        else:
                            return render(request,"nuevareservacion.html",{
                                "form": ReservacionForm,
                                "msg": "Ustede debe autenticarse "
                        }) 
                else:
                        return render(request,"nuevareservacion.html",{
                                "form": ReservacionForm,
                                "msg": "este formulario no es valido"
                        })
           except Exception as e:
                return render(request,"nuevareservacion.html",{
                                "form": ReservacionForm,
                                "msg": f"Hubo un error {e}"
                        })