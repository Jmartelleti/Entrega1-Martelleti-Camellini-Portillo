from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django import forms
from django.contrib.auth.models import User


#el formulario para poder registrarse
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#Form para actualizar el usuario
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

#El formulario para poder actualizar la imagen de perfil o avatar
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
