from django.db import models
from django.db.models.base import Model
from django.db.models.fields import IntegerField, TextField
from django.db.models.fields.related import ManyToManyField

# Create your models here.

#Modelo Clima para almacenar todos los posibles climas
class Clima(models.Model):
    nombre=models.TextField()

#Modelo Region en este se almacenaran las regiones productoras de cafe
class Region(models.Model):
    nombre=models.TextField()
    caracteristicas=models.TextField()
    clima=models.ForeignKey(Clima, on_delete=models.CASCADE)
    temperatura=models.TextField()
    altitud=models.IntegerField()
    demografia=models.IntegerField()

#modelo Productor para almacenar los datos de cada productor
class Productor(models.Model):
    nombre=models.TextField()
    apellidos=models.TextField()
    email=models.EmailField()
    telefono=models.IntegerField()
    facebook=models.TextField()
    region=models.ForeignKey(Region,on_delete=models.CASCADE)
    password=models.TextField()

#Modelo Producto almacena los datos de todos los productos de cada productor
class Producto(models.Model):
    nombre=models.TextField()
    descripcion=models.TextField()
    variedad=models.TextField()
    tipo_produccion=models.TextField()

class Presentacion(models.Model):
    id_producto=models.IntegerField()
    descripcion=models.TextField()
    costo=models.FloatField()

class Imagen(models.Model):
    id_producto=models.IntegerField()
    imagen=models.ImageField()



