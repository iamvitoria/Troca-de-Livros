from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('conversas/', ConversasView.as_view(), name='conversas'),
    path('chat/<str:email>/', ChatView.as_view(), name='chat'),
    
    path('mensagens/', MensagemListView.as_view(), name='mensagem-list'),
    path('mensagens/delete/<int:pk>/', MensagemDeleteView.as_view(), name='mensagem-delete'),
]
