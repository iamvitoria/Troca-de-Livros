from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('perfil', ProfileView.as_view(), name='perfil'),
]
