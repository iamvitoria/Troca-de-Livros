from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('listar_livro/', LivroListView.as_view(), name='listar_livro'),
    path('adicionar_livro/', LivroCreateView.as_view(), name='adicionar_livro'),
]
