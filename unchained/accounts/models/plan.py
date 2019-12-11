from django.db import models
from . import Gym, Profile


class Plan(models.Model):
	nome = models.CharField(max_length=30)
	valor= models.FloatField()
	incluso = models.TextField()
	academia = models.ForeignKey(Gym, on_delete=models.CASCADE, related_name="planos")
	compradores = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="planos")
	