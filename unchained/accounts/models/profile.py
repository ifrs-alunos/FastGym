from django.db import models
from .gym import Gym

class Profile(models.Model):
	owner = models.OneToOneField('auth.user', on_delete=models.CASCADE)
	telefone = models.CharField(max_length=16)
	cpf = models.CharField(max_length=11)
	rg = models.CharField(max_length=9)
	nascimento = models.DateField()
	endereco = models.CharField(max_length=80)
	academias = models.ManyToManyField(Gym, related_name="profiles", blank=True)
	sexo = models.CharField(max_length=9, choices=[('masculino','Masculino'),('feminino','Feuinino')])


	