from django.db import models
from . import Usuario

class Cartao(models.Model):
	bandeira = models.CharField(max_length=15)
	numero = models.CharField(max_length=30)
	usuario = models.ForeignKey(Usuario, related_name="cartoes", on_delete=models.CASCADE)