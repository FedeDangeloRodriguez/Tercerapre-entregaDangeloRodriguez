from django.db import models

# Create your models here.

class Equipo(models.Model):

    nombre = models.CharField(max_length=30)
    barrio = models.CharField(max_length=30)
    titulos = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} de {self.barrio}"
    
class Jugador(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}, {self.edad} años."

class Entrenadores(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    titulos = models.IntegerField()
    edad = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}, {self.edad} años."