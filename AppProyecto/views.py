from django.shortcuts import render
from .models import Familia
from django.http import HttpResponse

# Create your views here.

def familiar(request):
    familiar1 = Familia(nombre = "Sandra", fecha_nacimiento = 31/12/1995, dni = 20567865 )
    familiar1.save()
    familiar2 = Familia(nombre = "Ivan", fecha_nacimiento = 26/7/2000, dni = 45794302)
    familiar2.save()
    familiar3 = Familia(nombre = "Enrique", fecha_nacimiento = 20/9/1993, dni = 20730184)
    familiar3.save()
    lista_familiares = [familiar1, familiar2, familiar3]

    return render(request,"AppProyecto/template.html", {"cursos" : lista_familiares})
    return HttpResponse()

