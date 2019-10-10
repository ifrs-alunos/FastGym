from django.db import models

class Academia(modesl.Model):
	nome = models.CharField(max_lenght="40")
	telefone = models.CharField(max_lenght="16")
	email = models.EmailField()
	endereco = models.CharField(max_lenght="80")
	associados = models.IntegerField()