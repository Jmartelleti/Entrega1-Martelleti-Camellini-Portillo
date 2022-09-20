from dataclasses import field
from django import forms
from .models import Usuario

class usuarioForm(forms.Form):
    usuario=forms.CharField(max_length=50)
    email=forms.EmailField(max_length=2000000)
    password1=forms.CharField(label="Ingrese la contraseña:", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repita la contraseña", widget=forms.PasswordInput)

    class Meta: 
        model = Usuario
        fields = ["usuario", "password1", "email", "password2"]


class contactForm(forms.Form):
    nombre=forms.CharField(max_length=45)
    phone=forms.IntegerField(max_value=20000000)
    email=forms.EmailField(max_length=100)
    mensaje=forms.CharField(max_length=300)
    
class articleForm(forms.Form):
    usuario=forms.CharField(max_length=45)
    articuloTitulo=forms.CharField(max_length=50)
    articuloContenido=forms.CharField(max_length=200)

class AvatarForm(forms.Form):
    imagen=forms.ImageField
