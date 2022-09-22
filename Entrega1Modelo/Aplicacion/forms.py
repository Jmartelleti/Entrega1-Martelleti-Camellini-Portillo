from dataclasses import field
import email
from django import forms
from .models import Usuario

class usuarioForm(forms.Form):
    username=forms.CharField(max_length=50)
    email=forms.EmailField(max_length=2000000)
    password1=forms.CharField(label="Ingrese la contraseña:", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repita la contraseña", widget=forms.PasswordInput)

    class Meta: 
        model = Usuario
        fields = ["username", "password1", "email", "password2"]

class UserEditForm(usuarioForm):
    email=forms.EmailField(label="Modificar Email")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="repita la contraseña", widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ["email", "password1", "password2", ]
        help_text = {k: "" for k in fields}

class UserRegisterForm(usuarioForm):
    email= forms.EmailField()
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repita contraseña",widget=forms.PasswordInput)

    last_name=forms.CharField()
    first_name=forms.CharField()

    class Meta:
        model = Usuario
        fields=["username","email","password1","password2", "last_name","first_name"]
        help_texts= {k:"" for k in fields}



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
    img=forms.ImageField
