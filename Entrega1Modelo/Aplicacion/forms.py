from django import forms

class usuarioForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    comision=forms.IntegerField(max_value=2000000)

class AForm(forms.Form):
    nombre=forms.CharField(max_length=45)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField(max_length=100)
    profesion=forms.CharField(max_length=25)