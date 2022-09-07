import email
from uuid import RESERVED_FUTURE
from Aplicacion.forms import contactForm, usuarioForm, articleForm
from django.shortcuts import render
from .models import Usuario, Contacto, Articulo
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    if request.method=="POST":
        form=usuarioForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            usuario1=Usuario(usuario=informacion["usuario"], email=informacion["email"], password=informacion["password"] )
            usuario1.save()
            return render (request,"Aplicacion/index.html", {"mensaje":"USUARIO"} )
    else:
        formulario=usuarioForm()
        return render(request,"Aplicacion/index.html", {"formulario":formulario})
    
def usuarioBusqueda(request):
    return render(request, "Aplicacion/usuarioBusqueda.html")

def usuarioResultado(request):
    if request.GET["usuario"]:
        usuario=request.GET["usuario"]
        usuario1=Usuario.objects.filter(usuario=usuario)
        return render(request, "Aplicacion/usuarioResultados.html", {"usuario1":usuario1})

    return render (request, "Aplicacion/usuarioBusqueda.html")

def about(request):
    return render(request, "Aplicacion/about.html")

def post(request):
    if request.method=="POST":
        form=articleForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            usuario=Articulo(usuario=informacion["usuario"], articuloTitulo=informacion["articuloTitulo"], articuloContenido=informacion["articuloContenido"])
            usuario.save()
            return render(request, "Aplicacion/post.html", {"mensaje":"Mensaje Enviado"})
    else: 
        form=articleForm()
        return render(request, "Aplicacion/post.html", {"form":form})

def articuloBusqueda(request):
    return render(request,"Aplicacion/articuloBusqueda.html")

def articuloResultados(request):
    if request.GET["usuario"]:
        usuario=request.GET["usuario"]
        usuarios=Articulo.objects.filter(usuario=usuario)
        return render(request,"Aplicacion/articuloResultados.html", {"usuarios":usuarios})

def contact(request):
    if request.method=="POST":
        form=contactForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            contacto=Contacto(nombre=informacion["nombre"], phone=informacion["phone"], email=informacion["email"], mensaje=informacion["mensaje"] )
            contacto.save()
            return render (request,"Aplicacion/contact.html", {"mensaje":"Mensaje Enviado"} )
    else:
        formulario=contactForm()
        return render(request,"Aplicacion/contact.html", {"formulario":formulario})

def buscarContact(request):
    if request.GET["email"]:
        email=request.GET["email"]
        usuario=Contacto.objects.filter(email=email)
        return render(request, "Aplicacion/contactResultados.html", {"usuario":usuario})
    else:
        return render(request, "Apicacion/contactBusqueda.html", {"mensaje":"ingrese una opcion"})   

def contactBusqueda(request):
    return render(request, "Aplicacion/contactBusqueda.html")   

def post1(request):
    return render(request, "Aplicacion/post1.html")

def post2(request):
    return render(request, "Aplicacion/post2.html")

def post3(request):
    return render(request, "Aplicacion/post3.html")

def post4(request):
    return render(request, "Aplicacion/post4.html")

