from django.views.generic import TemplateView, ListView
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.views.generic import ListView
from django.db.models import Q
from .models import Mensagem

class ConversasView(ListView):
    model = Mensagem
    template_name = 'conversas.html'
    context_object_name = 'conversas'

    def get_queryset(self):
        remetente_email = self.request.user.email  # Obtém o email do usuário autenticado

        # Busca todos os destinatários únicos com quem o usuário autenticado trocou mensagens
        destinatarios = Mensagem.objects.filter(remetente_email=remetente_email).values_list('destinatario_email', flat=True).distinct()

        # Lista para armazenar informações resumidas de cada conversa
        conversas = []

        # Para cada destinatário, busca a última mensagem trocada
        for destinatario in destinatarios:
            ultima_mensagem = Mensagem.objects.filter(
                Q(remetente_email=remetente_email, destinatario_email=destinatario) |
                Q(remetente_email=destinatario, destinatario_email=remetente_email)
            ).order_by('-data_envio').first()

            if ultima_mensagem:
                # Cria um dicionário com informações resumidas da conversa
                conversa = {
                    'destinatario': destinatario,
                    'ultima_mensagem': ultima_mensagem.descricao,
                    'data_envio': ultima_mensagem.data_envio
                }
                conversas.append(conversa)

        conversas.sort(key=lambda x: x['data_envio'], reverse=True)

        return conversas

class ChatView(TemplateView):
    template_name = 'chat.html'
    context_object_name = 'mensagens'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        remetente_email = self.request.user.email  # Assumindo que você está usando o usuário autenticado
        destinatario_email = self.kwargs['email']

        # Busca todas as mensagens trocadas entre o remetente e o destinatário
        mensagens_enviadas = Mensagem.objects.filter(remetente_email=remetente_email, destinatario_email=destinatario_email)
        mensagens_recebidas = Mensagem.objects.filter(remetente_email=destinatario_email, destinatario_email=remetente_email)

        # Combina e ordena as mensagens por data de envio
        mensagens = list(mensagens_enviadas) + list(mensagens_recebidas)
        mensagens.sort(key=lambda x: x.data_envio)

        context['mensagens'] = mensagens
        context['email'] = destinatario_email  # Passa o email do destinatário para o template
        context['user'] = self.request.user  # Passa o objeto do usuário autenticado para o template
        return context

    def post(self, request, *args, **kwargs):
        remetente_email = request.POST.get('remetente_email')
        destinatario_email = request.POST.get('destinatario_email')
        descricao = request.POST.get('descricao')

        # Cria uma nova instância de Mensagem e salva no banco de dados
        mensagem = Mensagem(
            remetente_email=remetente_email,
            destinatario_email=destinatario_email,
            descricao=descricao
        )
        mensagem.save()

        # Redireciona de volta para a mesma página após o envio da mensagem
        return HttpResponseRedirect(reverse('chat', kwargs={'email': destinatario_email}))
