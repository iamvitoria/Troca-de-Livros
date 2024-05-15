from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario
from .forms import UsuarioForm

class CustomUsuarioAdmin(UserAdmin):
    model = Usuario
    form = UsuarioForm
    list_display = ('email', 'nome', 'idade', 'cpf', 'endereco', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('nome', 'idade', 'cpf', 'cep')}),
        ('Endereço', {'fields': ('endereco', 'numero', 'complemento', 'bairro', 'cidade', 'estado')}), # Adicionei os campos de endereço aqui
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nome', 'idade', 'cpf', 'cep', 'endereco', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'nome', 'cpf')
    ordering = ('email',)

    filter_horizontal = ()
    list_filter = ()

    def save_model(self, request, obj, form, change):
        if not change:
            obj.cep = form.cleaned_data.get('cep')
        super().save_model(request, obj, form, change)

admin.site.register(Usuario, CustomUsuarioAdmin)
