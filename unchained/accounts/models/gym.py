from django.db import models

class Gym(models.Model):
	owner = models.OneToOneField('auth.User', on_delete=models.CASCADE)
	cnpj = models.CharField(max_length=40)
	telefone = models.CharField(max_length=16)
	endereco = models.CharField(max_length=80)
	associados = models.IntegerField()