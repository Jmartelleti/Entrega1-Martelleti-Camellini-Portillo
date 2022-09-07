from django import forms

class usuarioForm(forms.Form):
    usuario=forms.CharField(max_length=50)
    email=forms.EmailField(max_length=2000000)
    password=forms.CharField(widget=forms.PasswordInput)


class contactForm(forms.Form):
    nombre=forms.CharField(max_length=45)
    phone=forms.IntegerField(max_value=20000000)
    email=forms.EmailField(max_length=100)
    mensaje=forms.CharField(max_length=300)
    
class articleForm(forms.Form):
    usuario=forms.CharField(max_length=45)
    articuloTitulo=forms.CharField(max_length=50)
    articuloContenido=forms.CharField(max_length=200)
