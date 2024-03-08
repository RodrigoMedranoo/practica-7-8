from django.forms import ModelForm
from .models import Reservacion

class ReservacionForm(ModelForm):
    class Meta:
        model= Reservacion
        fields= [
            'id_pelicula',
            'nombre_pelicula',
            'asientos',
            'no_adultos',
            'no_menores'
        ]