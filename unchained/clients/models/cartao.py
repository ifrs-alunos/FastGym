from django.db import models
from user import User

class Cartao(models.Model):
	bandeira = models.CharField(max_lenght="15")
	numero = models.CharField(max_lenght="30")
	usuario = models.ForeignKey('User', related_name="cartoes", on_delete=models.CASCADE)