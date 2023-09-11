from django.db import models

# Create your models here.

class Cuso(models.Model):
    
    nombre = models.CharField( max_length=40)
    camada = models.IntegerField()
    
class Estudiante(models.Model):
    
    nombre = models.CharField( max_length=40)
    camada = models.IntegerField()   
    email = models.EmailField(max_length=30)    

class Estudiante(models.Model):
    
    nombre = models.CharField( max_length=40)
    camada = models.IntegerField()   
    email = models.EmailField(max_length=30)
    profession = models.CharField(max_length=20)
    
class Estudiante(models.Model):
    
    nombre = models.CharField( max_length=40)
    fecha_entraga = models.DateField()
    entregado = models.BooleanField()
    
    
    

    
