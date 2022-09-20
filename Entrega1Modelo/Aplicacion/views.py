import email
from uuid import RESERVED_FUTURE
from Aplicacion.forms import contactForm, usuarioForm, articleForm, AvatarForm
from django.shortcuts import render
from .models import Usuario, Contacto, Articulo, Avatar
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

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
        return render(request,"Aplicacion/contact.html", {"formulario":formulario, "avatar":AgregarAvatar(request.user)})

def buscarContact(request):
    if request.GET["email"]:
        email=request.GET["email"]
        usuario=Contacto.objects.filter(email=email)
        return render(request, "Aplicacion/contactResultados.html", {"usuario":usuario})
    else:
        return render(request, "Apicacion/contactBusqueda.html", {"mensaje":"ingrese una opcion", "avatar":AgregarAvatar(request.user)})   

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

@login_required
def editarUsuario(request):
    usuario=request.usuario

def login(request):
    return render(request, "Aplicacion/login.html")

def AgregarAvatar(request):
    if request.method=="POST":
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatarviejo=Avatar.objects.filter(user=request.user)
            if len(avatarviejo)>0:
                avatarviejo[0].delete()
                avatar=Avatar(user=request.user, imagen=formulario.cleaned_data["imagen"])
                avatar.save()
                return render (request, inicio, {"usuario":request.user,"mensaje":avatar,"imagen":avatar.imagen.url})