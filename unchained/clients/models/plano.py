from django.db import models
from . import Academia, Usuario


class Plano(models.Model):
	nome = models.CharField(max_length=30)
	valor= models.FloatField()
	incluso = models.TextField()
	academia = models.ForeignKey(Academia,on_delete=models.CASCADE , related_name="planos")
	compradores = models.ForeignKey(Usuario,on_delete=models.CASCADE , related_name="planos")
	