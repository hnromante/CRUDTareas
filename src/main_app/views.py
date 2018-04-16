from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Tarea
from .forms import TareaForm
# Create your views here.

def index(request):
    return render(request,'base_main_app.html')

def tareas(request):
    listado_tareas = Tarea.objects.all()
    form = TareaForm()
    return render(request,'tareas.html',{'tareas':listado_tareas,'form':form})

def detalle(request,id_tarea):
    tarea = Tarea.objects.get(pk=id_tarea)
    return render(request,'detalle.html',{'tarea':tarea})

def agregar_tarea(request):
    form =  TareaForm(request.POST)
    tarea = Tarea (
        nombre = form.cleaned_data['nombre'],
        descripcion = form.cleaned_data['descripcion'],
        inicio = form.cleaned_data['inicio'],
        termino = form.cleaned_data['termino'],
        estado = form.cleaned_data['estado'],
        img = form.cleaned_data['img'],
    )
    tarea.save()
    return HttpResponseRedirect('/tareas')