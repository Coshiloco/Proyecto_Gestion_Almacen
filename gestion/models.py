import email
from unicodedata import name
from django.db import models

# Create your models here.


class Cliente(models.Model):
    idcliente = models.CharField(max_length=500)
    nombrecompania = models.CharField(max_length=500)
    direccionfacturacion = models.CharField(max_length=500)
    ciudad = models.CharField(max_length=500)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
