from django.urls import path
from .views import *

urlpatterns = [
    
    path("", inicio, name="inicio"),
    path("about.html/", about, name="about"),
    path("post.html/", post, name="post"),
    path("contact.html/", contact, name="contact"),



]
