from django import forms

from mi_app.models import Curso, Estudiante, Profesor, Familiares, Entregable

class CursoFormulario(forms.Form):
    #Especificar los campos
    curso = forms.CharField()
    camada = forms.IntegerField()

class CursoBusqueda(forms.Form):
    criterio = forms.CharField()

class EstudianteFormulario(forms.Form):
    #Especificar los campos
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class FamiliarFormulario(forms.Form):
    #Especificar los campos
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()