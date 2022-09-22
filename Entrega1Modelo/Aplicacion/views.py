import email
from urllib.request import Request
from uuid import RESERVED_FUTURE
from Aplicacion.forms import contactForm, usuarioForm, articleForm, AvatarForm, UserEditForm, UserRegisterForm
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

@login_required    
def usuarioBusqueda(request):
    return render(request, "Aplicacion/usuarioBusqueda.html")

@login_required
def usuarioResultado(request):
    if request.GET["usuario"]:
        usuario=request.GET["usuario"]
        usuario1=Usuario.objects.filter(usuario=usuario)
        return render(request, "Aplicacion/usuarioResultados.html", {"usuario1":usuario1})

    return render (request, "Aplicacion/usuarioBusqueda.html")
@login_required
def about(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        avatar=lista[0].img.url#url de la imagen del avatar
    else:
        avatar=""
    return render(request, "Aplicacion/about.html", {"avatar":avatar})

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

@login_required
def articuloBusqueda(request):
    return render(request,"Aplicacion/articuloBusqueda.html")

@login_required
def articuloResultados(request):
    if request.GET["username"]:
        usuario=request.GET["username"]
        usuarios=Articulo.objects.filter(username=usuario)
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

@login_required
def buscarContact(request):
    if request.GET["email"]:
        email=request.GET["email"]
        usuario=Contacto.objects.filter(email=email)
        return render(request, "Aplicacion/contactResultados.html", {"usuario":usuario})
    else:
        return render(request, "Apicacion/contactBusqueda.html", {"mensaje":"ingrese una opcion", "avatar":AgregarAvatar(request.user)})   

@login_required
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
    usuario=request.user
    if request.method=="POST":
        form= UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.save()
            return render (request, "Aplicacion/index.html", {"mensaje":"Usuario editado correctamente."})
    else:
        form=UserEditForm(initial={ "email":usuario.email})#o instance=usuario
        return render(request, "Aplicacion/editarUsuario.html", {"form":form, "usuario":usuario})

def login_request(request):
    if request.method == "POST":
        formulario=AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario=formulario.cleaned_data["username"]
            contraseña=formulario.cleaned_data["password"]

            user= authenticate(username=usuario, password=contraseña)

            if user is not None:
                login(request, user)
                return render(request, "Aplicacion/index.html", {"mensaje":f"Bienvenido {usuario}!!"})
            else:
                return render(request, "Aplicacion/register.html", {"mensaje":"Error, datos incorrecto"})
        else:
            return render (request,"Aplicacion/login.html", {"mensaje":"Error formulario erroneo", "formulario":formulario})
    formulario=AuthenticationForm()
    return render(request, "Aplicacion/login.html", {"formulario":formulario})          
""" 
def register(request):

    if request.method == "POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.username=info[]
            form.save()
            return render(request,"Aplicaicon/index.html", {"mensaje":"Usuario Creado"})
    else:
        form=UserRegisterForm()
        return render(request, "Aplicacion/register.html", {"form":form}) """















""" def AgregarAvatar(request):
    if request.method=="POST":
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatarviejo=Avatar.objects.filter(user=request.user)
            if len(avatarviejo)>0:
                avatarviejo[0].delete()
                avatar=Avatar(user=request.user, imagen=formulario.cleaned_data["imagen"])
                avatar.save()
                return render (request, inicio, {"usuario":request.user,"mensaje":avatar,"imagen":avatar.imagen.url})
 """


