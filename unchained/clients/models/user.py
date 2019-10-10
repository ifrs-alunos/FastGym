from django.db import models
from academia import Academia

class User(mmodels.Model):
	nome = models.CharField(max_lenght="40")
	telefone = models.CharField(max_lenght="16")
	email = models.EmailField()
	cpf = models.CharField(max_lenght="11")
	rg = models.CharField(max_lenght="9")
	nascimento = models.DateField()
	endereco = models.CharField(max_lenght="80")
	academias = models.ManyToManyField('Academia', related_name="usuarios")
	