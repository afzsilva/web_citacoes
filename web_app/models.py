from django.db import models

# Create your models here.
class ScrapData(models.Model):
    nome_autor = models.CharField(max_length=100,null=False, blank=False)
    citacao = models.CharField(max_length=255,null=False, blank=False)