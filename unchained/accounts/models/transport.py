from django.db import models
from . import Gym

class Transport(models.Model):
	nome = models.CharField(max_length=40)
	tipo = models.CharField(max_length=40)
	contato = models.TextField()
	academia = models.ManyToManyField(Gym, related_name="transportes")