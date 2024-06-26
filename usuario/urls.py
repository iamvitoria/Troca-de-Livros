from django.urls import path
from .views import ProfileView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("perfil/", ProfileView.as_view(), name="perfil"),
    path("perfil/editar", views.editar_perfil, name="editar_perfil"),
    path("usuarios/", views.lista_usuarios, name="lista_usuarios"),
    path(
        "usuarios/excluir/<int:usuario_id>/",
        views.excluir_usuario,
        name="excluir_usuario",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
