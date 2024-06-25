from django.urls import path
from .views import ProfileView
from . import views

urlpatterns = [
    path("perfil/", ProfileView.as_view(), name="perfil"),
    path("perfil/editar", views.editar_perfil, name="editar_perfil"),
    path("usuarios/", views.lista_usuarios, name="lista_usuarios"),
    path(
        "usuarios/excluir/<int:usuario_id>/",
        views.excluir_usuario,
        name="excluir_usuario",
    ),
]
