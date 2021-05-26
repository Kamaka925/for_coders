from django.db import models

# Create your models here.

class Operacao(models.Model):
    loja = models.CharField(max_length=22)
    dono = models.CharField(max_length=18)
    tipo = models.CharField(max_length=25)
    cartao = models.CharField(max_length=15)
    cpf = models.CharField(max_length=14)
    valor = models.CharField(max_length=13)
    data = models.CharField(max_length=13)
    hora = models.CharField(max_length=11)
    total = models.CharField(max_length=6)
