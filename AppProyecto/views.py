from django.shortcuts import render
from .models import Familia
from django.http import HttpResponse

# Create your views here.

def familiar(request):
    familiar1 = Familia(nombre_apellido = "Sandra Fernandez", año_nacimiento = 1995, dni = 20567865 )
    familiar1.save()
    familiar2 = Familia(nombre_apellido = "Ivan Perez", año_nacimiento = 2000, dni = 45794302)
    familiar2.save()
    familiar3 = Familia(nombre_apellido = "Enrique Perez", año_nacimiento = 1993, dni = 20730184)
    familiar3.save()
    lista_familiares = [familiar1, familiar2, familiar3]

    return render(request,"familia.html", {"familiares" : lista_familiares})
    return HttpResponse()

