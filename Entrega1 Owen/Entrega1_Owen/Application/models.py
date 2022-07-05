from django.db import models

# Create your models here.

class Producto(models.Model):

    nombre = models.CharField(max_length= 25)
    serie = models.IntegerField(max_length=10)
    tipo = models.CharField(max_length=10)

class Vendedor(models.Model):

    nombre = models.CharField(max_length= 25)
    apellido = models.CharField(max_length= 25)
    cuil = models.IntegerField()
    DNI = models.IntegerField()

class Cliente(models.Model):
    nombre = models.CharField(max_length= 25)
    apellido = models.CharField(max_length= 25)
    telefono = models.IntegerField()