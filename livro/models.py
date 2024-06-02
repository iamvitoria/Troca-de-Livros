from django.db import models
from django.contrib.auth.models import User

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data_publicacao = models.DateField()

    def __str__(self):
        return self.titulo
