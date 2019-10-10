from django.db import models
from .reporter import Reporter

class Article(models.Model):
    title=models.CharField(max_length=100)
    pud_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
