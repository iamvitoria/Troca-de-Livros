from django.db import models

class Mensagem(models.Model):
    remetente_email = models.CharField(max_length=200, default='null')
    destinatario_email = models.CharField(max_length=200, default='null')
    descricao = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Mensagem de {self.remetente_email} para {self.destinatario_email}'
