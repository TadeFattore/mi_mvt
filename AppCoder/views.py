from mimetypes import MimeTypes
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from AppCoder.models import Padres,Abuelos,Hermanos
from AppCoder.forms import AddAbuelos, AddPadres

# Create your views here.

def abuelos(request):
    if request.method == 'POST':
        miFormulario = AddAbuelos(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            abuelos = Abuelos(nombre=informacion['nombre'],paisDeNac=informacion['paisDeNac'],anioDeNac=informacion['anioDeNac'])
            abuelos.save()
            return render(request, "AppCoder/index.html")
    else:
        miFormulario = AddAbuelos()
    return render(request, "AppCoder/abuelos.html", {"miFormulario":miFormulario})      

def padres(request):
    if request.method == 'POST':
        miFormulario = AddPadres(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            padres = Padres(nombre=informacion['nombre'],paisDeNac=informacion['paisDeNac'],anioDeNac=informacion['anioDeNac'])
            padres.save()
            return render(request, "AppCoder/index.html")
    else:
        miFormulario = AddPadres()
    return render(request, "AppCoder/padres.html", {"miFormulario":miFormulario})      


def hermanos(request):
    return render(request, "AppCoder/hermanos.html")

def inicio(request):
    return render(request,"AppCoder/index.html")

def busquedaAbuelos(request):
    return render(request, "AppCoder/BusquedaAbuelos.html")

def buscarAbuelos(request):
    if request.GET['nombre']:
        nombre=request.GET['nombre']
        abuelos = Abuelos.objects.filter(nombre__iexact=nombre)

        return render(request, "AppCoder/resultadosBusqueda.html", {"abuelos":abuelos, "nombre":nombre})
    else:
        respuesta = "No ingresaste datos."
    return HttpResponse(respuesta)

def busquedaPadres(request):
    return render(request, "AppCoder/BusquedaPadres.html")

def buscarPadres(request):
    if request.GET['nombre']:
        nombre=request.GET['nombre']
        padres = Padres.objects.filter(nombre__iexact=nombre)

        return render(request, "AppCoder/resultadosBusquedaPadres.html", {"padres":padres, "nombre":nombre})
    else:
        respuesta = "No ingresaste datos."
    return HttpResponse(respuesta)