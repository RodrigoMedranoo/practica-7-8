from django.contrib import admin
from django.contrib import admin
from .models import Reservacion

# Register your models here.
class ReservacionAdmin(admin.ModelAdmin):
    readonly_fields=("fecha_creacion",)

admin.site.register(Reservacion,ReservacionAdmin)