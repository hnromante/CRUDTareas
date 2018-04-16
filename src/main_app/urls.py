from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^tareas/$', views.tareas, name='tareas'),
    url(r'^tareas/([0-9]+)/$', views.detalle, name='detalle')
]