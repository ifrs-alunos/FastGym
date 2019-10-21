from django.db import models
from .academia import Academia
from .user import User

class Produto(models.Model):
	nome = models.CharField(max_length=30)
	valor= models.FloatField()
	quantidade = models.IntegerField()
	descricao = models.TextField()
	academia = models.ForeignKey('Academia',on_delete=models.CASCADE , related_name="produtos")
	compradores = models.ForeignKey('User',on_delete=models.CASCADE , related_name="produtos")