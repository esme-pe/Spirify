#importaciones:
from django.shortcuts import render
from django.http import HttpResponse

# Clase de prueba:
def home_inicio(request):
    
    return HttpResponse("<h1>Titulo")



