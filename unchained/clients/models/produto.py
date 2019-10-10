from dajngo.db import models
from academia import Academia
from user import User

class Produto(models.Model):
	nome = models.CharField(max_lenght="30")
	valor= models.FloatField()
	quantidade = models.IntegerField()
	descricao = models.TextField()
	academia = models.ForeignKey('Academia', related_name="produtos")
	compradores = models.ForeignKey('User', related_name="produtos")