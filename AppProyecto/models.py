from django.db import models

# Create your models here.

class Familia(models.Model):
    nombre_apellido = models.CharField(max_length = 50)
    año_nacimiento = models.IntegerField()
    dni = models.IntegerField()



