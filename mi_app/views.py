from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime 

def saludo(request):
    fecha_hora_ahora = datetime.now()
    return HttpResponse(f'Hola mundo {fecha_hora_ahora}')

def saludar_a(request, nombre):
    return HttpResponse(f'Hola como estas {nombre.capitalize()}?')

    def mostrar_mi_template(request):
        return render(request, 'mi_app/index.html')



