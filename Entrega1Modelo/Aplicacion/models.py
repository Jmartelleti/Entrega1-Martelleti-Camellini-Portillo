from django.db import models

# Create your models here.

class usuario(models.Model):
    nombre=models.TextField(max_length=40)
    password=models.CharField(max_length=40)



