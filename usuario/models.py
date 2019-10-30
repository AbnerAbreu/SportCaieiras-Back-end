from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    confirmEmail = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    confirmSenha = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)

