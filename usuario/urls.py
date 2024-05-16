from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_usuario, name='usuario_login'),
    path('registro/', views.registro_usuario, name='usuario_registro'),
    path('index/', views.index, name='index'),  # Ajuste conforme sua configuração
]
