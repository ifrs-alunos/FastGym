from django.db import models

class Academia(models.Model):
	nome = models.CharField(max_length=40)
	telefone = models.CharField(max_length=16)
	email = models.EmailField()
	endereco = models.CharField(max_length=80)
	associados = models.IntegerField()