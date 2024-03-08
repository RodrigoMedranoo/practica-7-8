from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Reservacion(models.Model):
    id_pelicula= models.IntegerField()
    nombre_pelicula= models.CharField(max_length = 512)
    asientos = models.IntegerField()
    no_adultos= models.IntegerField()
    no_menores= models.IntegerField()
    fecha_creacion= models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.nombre_pelicula} - {self.no_adultos} adultos - {self.no_menores} menores'