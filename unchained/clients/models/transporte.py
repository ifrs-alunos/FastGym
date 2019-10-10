from django.db import models
from academia import Academia

class Transporte(models.Model):
	nome = models.CharField(max_lenght="40")
	tipo = models.CharField(max_lenght="40")
	contato = models.TextField()
	academia = models.ManyToManyField("Academia", related_name="transportes")