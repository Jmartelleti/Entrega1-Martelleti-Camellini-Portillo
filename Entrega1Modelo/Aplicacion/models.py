from django.db import models

# Create your models here.

class Usuario(models.Model):
    usuario=models.TextField(max_length=40)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=40)

    def __str__(self):
        return f"{self.usuario}, {self.email}."


class Contacto(models.Model):
    nombre=models.CharField(max_length=45)
    phone=models.IntegerField()
    email=models.EmailField(max_length=100)
    mensaje=models.TextField(max_length=300)

    def __str__(self) -> str:
        return f"{self.nombre}, contacto {self.email} numero: {self.phone}. MENSAJE: {self.mensaje}"

class Articulo(models.Model):
    usuario=models.CharField(max_length=50)
    articuloTitulo=models.TextField(max_length=50)
    articuloContenido=models.TextField(max_length=200)

    def __str__(self):
        return f"{self.usuario} recomienda subir articulo de: {self.articuloTitulo}"




