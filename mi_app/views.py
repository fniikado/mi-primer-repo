from pydoc import doc
from unittest import loader
from xml.dom import minidom
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from mi_app.models import *
from mi_app.forms import *

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

def cursoFormulario(request):

    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST) #Aqui me llega toda la informacion del HTML

        print(miFormulario)

        if miFormulario.is_valid: #Si paso la validacion de Django
            informacion = miFormulario.cleaned_data

            cursos = Curso(nombre=informacion['curso'], camada=informacion['camada'])
            cursos.save()

            return render(request, "mi_app/cursoFormulario.html") #Vuelvo al inicio o a donde quieran
    
    else:
        miFormulario = CursoFormulario() #Formulario vacio para construir el HTML
    
    return render(request, "mi_app/cursoFormulario.html", {"miFormulario":miFormulario})

def formulario_busqueda(request):
    
    busqueda_formulario = CursoBusqueda()

    if request.GET:
        cursos = Curso.objects.filter(nombre=busqueda_formulario["criterio"]).all()
        return render(request, "mi_app/busqueda_curso.html", {"cursos" : cursos})

    return render(request, "mi_app/busqueda_curso.html", {"busqueda_formulario":busqueda_formulario})


def estudianteFormulario(request):

    if request.method == 'POST':
        miFormulario = EstudianteFormulario(request.POST) #Aqui me llega toda la informacion del HTML

        print(miFormulario)

        if miFormulario.is_valid: #Si paso la validacion de Django
            informacion = miFormulario.cleaned_data

            estudiante = Estudiante (nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])

            estudiante.save()

            return render(request, "mi_app/estudianteFormulario.html") #Vuelvo al inicio o a donde quieran
    
    else:
        miFormulario = EstudianteFormulario() #Formulario vacio para construir el HTML
    
    return render(request, "mi_app/estudianteFormulario.html", {"miFormulario":miFormulario})


def familiarFormulario(request):
    if request.method == 'POST':
        miFormulario = FamiliarFormulario(request.POST) #Aqui me llega toda la informacion del HTML

        print(miFormulario)

        if miFormulario.is_valid: #Si paso la validacion de Django
            informacion = miFormulario.cleaned_data

            familiar = Familiares (nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'])

            familiar.save()

            return render(request, "mi_app/familiares.html") #Vuelvo al inicio o a donde quieran
    
    else:
        miFormulario = FamiliarFormulario() #Formulario vacio para construir el HTML
    
    return render(request, "mi_app/familiarFormulario.html", {"miFormulario":miFormulario})

            