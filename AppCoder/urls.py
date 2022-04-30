from os import urandom
from django.urls import path
from AppCoder import views


urlpatterns = [

    path("abuelos/",views.abuelos,name="Abuelos"),
    path("padres/",views.padres ,name="Padres"),
    path("hermanos/",views.hermanos ,name="Hermanos"),
    path("",views.inicio,name="Inicio"),
    path("buscarAbuelos/",views.buscarAbuelos, name="BuscarAbuelos"),
    path("busquedaAbuelos/", views.busquedaAbuelos, name="BusquedaAbuelos"),
    path("buscarPadres/",views.buscarPadres, name="BuscarPadres"),
    path("busquedaPadres/", views.busquedaPadres, name="BusquedaPadres"),
]