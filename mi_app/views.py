from django.shortcuts import render

from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')

def actividades(request):
    return render(request, 'actividades.html')

def diagnostico(request):
    return render(request, 'diagnostico.html')

def galeria(request):
    return render(request, 'galeria.html')
