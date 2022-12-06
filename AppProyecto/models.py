from django.db import models

# Create your models here.

class Familia(models.Model):
    nombre_apellido = models.CharField(max_length = 50)
    fecha_nacimiento = models.DateField(default= 14/5/2001)
    dni = models.IntegerField()



