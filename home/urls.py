from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('perfil/', PerfilView.as_view(), name='perfil'),
    path('conversas/', ConversasView.as_view(), name='conversas'),
    path('meusitens/', MeusItensView.as_view(), name='meusitens'),
]