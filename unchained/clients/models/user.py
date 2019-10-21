from django.db import models
from .academia import Academia

class User(models.Model):
	nome = models.CharField(max_length=40)
	telefone = models.CharField(max_length=16)
	email = models.EmailField()
	cpf = models.CharField(max_length=11)
	rg = models.CharField(max_length=9)
	nascimento = models.DateField()
	endereco = models.CharField(max_length=80)
	academias = models.ManyToManyField('Academia', related_name="usuarios")
	