from uuid import RESERVED_FUTURE
from Aplicacion.forms import AForm, usuarioForm
from django.shortcuts import render
from .models import usuario
from django.http import HttpResponse
# Create your views here.

def usuario(request):
    if request.method=="POST":
        form=usuarioForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            profesor=usuario(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], profesion=informacion["profesion"] )
            profesor.save()
            return render (request,"Aplicacion/index.html", {"mensaje":"profesor creado"} )
    else:
        formulario=usuarioForm()
        return render(request,"Aplicacion/.html", {"formulario":formulario})


def buscar(request):
    if request.GET["comision"]:
        comision=request.GET["comision"]
        cursos=usuario.objects.filter(comision__icontains=comision)
        return render(request, "Aplicacion/resultadosBusqueda.html", {"cursos":cursos})
    else:
        return render(request, "Apicacion/busquedaComision.html", {"mensaje":"ingrese una opcion"})

def inicio(request):
    return render(request, "Aplicacion/index.html")

def about(request):
    return render(request, "Aplicacion/about.html")

def post(request):
    return render(request, "Aplicacion/post.html")

def contact(request):
    return render(request, "Aplicacion/contact.html")