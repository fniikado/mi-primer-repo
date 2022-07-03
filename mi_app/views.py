from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime

from mi_app.models import Estudiante, Curso, Familiares

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

def listar_cursos(request):
    context={}
    context["cursos"] = Curso.objects.all()
    return render(request, "mi_app/cursos.html", context)

def listar_familiares(request):
    context = {
        "familiares" : Familiares.objects.all(),
    }
    return render(request, "mi_app/familiares.html", context)
