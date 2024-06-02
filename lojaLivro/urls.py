from django.contrib import admin
from django.urls import path, include
from usuario.views import login_usuario
from usuario.views import registro_usuario
#from home.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_usuario, name='usuario_login'),
    path('registro/', registro_usuario, name='usuario_registro'),
    path('tela-inicial/', include('livro.urls'))

]
