from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

class PerfilView(TemplateView):
    template_name = 'perfil.html'

class ConversasView(TemplateView):
    template_name = 'conversas.html'

class MeusItensView(TemplateView):
    template_name = 'meusitens.html'


