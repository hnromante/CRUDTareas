from django.shortcuts import render
from django.http import HttpResponse
from .models import Tarea
# Create your views here.

def index(request):
    return render(request,'base_main_app.html')

def tareas(request):
    listado_tareas = Tarea.objects.all()
    return render(request,'tareas.html',{'tareas':listado_tareas})

def detalle(request,id_tarea):
    tarea = Tarea.objects.get(pk=id_tarea)
    return render(request,'detalle.html',{'tarea':tarea})

