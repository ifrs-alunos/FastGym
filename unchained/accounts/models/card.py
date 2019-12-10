from django.db import models
from . import Profile

class Card(models.Model):
	bandeira = models.CharField(max_length=15)
	numero = models.CharField(max_length=30)
	usuario = models.ForeignKey(Profile, related_name="cartoes", on_delete=models.CASCADE)