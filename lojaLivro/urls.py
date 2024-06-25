from django.contrib import admin
from django.urls import path, include
from usuario.views import login_usuario
from usuario.views import registro_usuario

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_usuario, name='usuario_login'),
    path('registro/', registro_usuario, name='usuario_registro'),
    path('tela-inicial/', include('livro.urls')),
    path('tela-inicial/', include('usuario.urls')),
    path('tela-inicial/', include('chat.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)