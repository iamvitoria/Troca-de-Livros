from django import forms
from .models import Usuario
import requests

class UsuarioForm(forms.ModelForm):
    cep = forms.CharField(label='CEP', max_length=9)

    class Meta:
        model = Usuario
        fields = ('email', 'nome', 'idade', 'cpf', 'cep', 'endereco', 'numero', 'complemento', 'bairro', 'cidade', 'estado')

    def clean_cep(self):
        cep = self.cleaned_data['cep']
        cep_url = f'http://viacep.com.br/ws/{cep}/json/'
        response = requests.get(cep_url)
        if response.status_code == 200:
            data = response.json()
            self.cleaned_data['endereco'] = data.get('logradouro', '')
            self.cleaned_data['numero'] = data.get('numero', '')
            self.cleaned_data['complemento'] = ''
            self.cleaned_data['bairro'] = data.get('bairro', '')
            self.cleaned_data['cidade'] = data.get('localidade', '')
            self.cleaned_data['estado'] = data.get('uf', '')
            return cep
        else:
            raise forms.ValidationError("CEP inválido")

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        cpf = cleaned_data.get("cpf")

        if Usuario.objects.filter(email=email).exists():
            self.add_error('email', forms.ValidationError("Este email já está em uso"))

        if Usuario.objects.filter(cpf=cpf).exists():
            self.add_error('cpf', forms.ValidationError("Este CPF já está em uso"))

        return cleaned_data
