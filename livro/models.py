from django.db import models
from django.contrib.auth.models import User

class Livro(models.Model):
    GENEROS_CHOICES = [
        ('fiction', 'Ficção'),
        ('non-fiction', 'Não Ficção'),
        ('romance', 'Romance'),
        ('mystery', 'Mistério'),
        # Adicione mais gêneros conforme necessário
    ]

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    ano_publicacao = models.IntegerField(default=2024)
    genero = models.CharField(max_length=20, choices=GENEROS_CHOICES, default='fiction')
    imagem = models.ImageField(upload_to='livros/', blank=True, null=True)

    def __str__(self):
        return self.titulo
