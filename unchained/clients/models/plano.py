from dajngo.db import models
from user import User

class Plano(models.Model):
	nome = models.CharField(max_lenght="30")
	valor= models.FloatField()
	incluso = models.TextField()
	academia = models.ForeignKey('Academia', related_name="planos")
	compradores = models.ForeignKey('User', related_name="planos")
	