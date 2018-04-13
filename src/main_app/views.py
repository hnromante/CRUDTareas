from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'base_main_app.html')

def tareas(request):
    return render(request,'tareas.html',{'tareas':listado_tareas})

class Tarea:
    def __init__(self,nombre,descripcion,inicio,termino,estado,img):
        self.nombre = nombre
        self.descripcion = descripcion
        self.inicio = inicio
        self.termino = termino
        self.estado = estado
        self.img = img

listado_tareas = [
    Tarea('Aprender Django','los fundamentos entre el jeuves y el sabado','hoy','sabado','pendiente','https://i.imgflip.com/1freth.jpg'),
    Tarea('Leer Pressman','capitulo 1 al 6, metodologias ágiles, scrum y spike','viernes','domingo','pendiente','https://i.imgflip.com/1freth.jpg'),
    Tarea('Crear app de tareas','aplicacion para gestionar tareas del grupo y de paso practicar Django','hoy','lunes','pendiente','https://i.imgflip.com/1freth.jpg'),

]

