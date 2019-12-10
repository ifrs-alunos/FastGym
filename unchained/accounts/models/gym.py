from django.db import models
from ..listas import lista_estados

class Gym(models.Model):
	owner = models.OneToOneField('auth.User', on_delete=models.CASCADE)
	cnpj = models.CharField(max_length=40)
	telefone = models.CharField(max_length=16)
	estado= models.CharField(max_length=30, choices=lista_estados)
	cidade = models.CharField(max_length=100)
	endereco = models.CharField(max_length=80)
	associados = models.IntegerField(default=0, blank=True)