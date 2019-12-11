from django.db import models
from accounts.models import  Gym, Profile

class Product(models.Model):
	nome = models.CharField(max_length=30)
	valor= models.FloatField()
	quantidade = models.IntegerField()
	descricao = models.TextField()
	academia = models.ForeignKey(Gym, on_delete=models.CASCADE, related_name="produtos")
	compradores = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="produtos")