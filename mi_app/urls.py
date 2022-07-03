from django.contrib import admin
from mi_app.views import (listar_familiares, saludo_personalizado, saludo, saludar_a, listar_estudiantes, 
listar_cursos,)
from django.urls import path

urlpatterns = [
    path('saludar/', saludo),
    path('saludar/persona/<nombre>', saludar_a),
    path('saludo_personalizado/', saludo_personalizado),
    path('estudiantes/', listar_estudiantes),
    path('cursos/', listar_cursos),
    path('familiares/', listar_familiares),
]
