from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime

from mi_app.models import Estudiante 

def saludo(request):
    fecha_hora_ahora = datetime.now()
    return HttpResponse(f'Hola mundo {fecha_hora_ahora}')

def saludar_a(request, nombre):
    return HttpResponse(f'Hola como estas {nombre.capitalize()}?')

def saludo_personalizado(request):
        context = {}
        if request.GET:
            context["nombre"] = request.GET["nombre"]
        
        return render(request, 'mi_app/index.html', context)


def listar_estudiantes(request):
    context = {
        "estudiantes": Estudiante.objects.all(),
    }
    return render(request, "mi_app/estudiantes.html", context)