from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)  #cria um campo numérico sequencial não duplicável
    nome = models.TextField(max_length=255)  
    idade = models.IntegerField()