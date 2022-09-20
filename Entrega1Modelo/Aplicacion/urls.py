from atexit import register
from django.urls import path
from .views import *

urlpatterns = [
    
    path("", inicio, name="inicio"),
    path("about.html/", about, name="about"),
    path("post.html/", post, name="post"),
    path("contact.html/", contact, name="contact"),
    path("post.html/post1/", post1, name="post1"),
    path("post.html/post2/", post2, name="post2"),
    path("post.html/post3/", post3, name="post3"),
    path("post.html/post4/", post4, name="post4"),
    path("usuario.html/",usuarioResultado, name="usuarioResultado"),
    path("usuarioBusqueda.html/", usuarioBusqueda, name="usuarioBusqueda"),
    path("contactBusqueda.html/", contactBusqueda, name="contactBusqueda"),
    path("contactResultados.html/",buscarContact, name="contactResultado"),
    path("articuloBusqueda.html/", articuloBusqueda, name="articleBusqueda"),
    path("articuloResultados.html/", articuloResultados, name="articleResultado"),
    path("login/", login, name="login"),
    
     





]
