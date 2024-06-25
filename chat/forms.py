# forms.py (crie este arquivo se ainda não existir)

from django import forms
from .models import Mensagem

class MensagemForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ['destinatario_email', 'descricao']
