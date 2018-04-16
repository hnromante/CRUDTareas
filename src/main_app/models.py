from django.db import models

# Create your models here.

class Tarea(models.Model):
    nombre = models.CharField(max_length = 50)
    descripcion = models.CharField(max_length = 50)
    inicio = models.DateTimeField()
    termino = models.DateTimeField(auto_now_add=False, blank=True,null=True)
   
    TERMINADA = 'terminada'
    PENDIENTE = 'pendiente'
    CANCELADA = 'cancelada'
    LIMITE = 'limite'
    ESTADOS_TAREAS = (
        (TERMINADA, 'Terminada'),
        (PENDIENTE, 'Pendiente'),
        (CANCELADA, 'Cancelada'),
        (LIMITE, 'Limite'),
    )
    estado = models.CharField(
        choices = ESTADOS_TAREAS,
        default = PENDIENTE,
        max_length = 30
    )
    img = models.CharField(max_length=255,blank=True)
                  
    def __str__(self):
        return self.nombre