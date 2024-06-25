from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('conversas/', ConversasView.as_view(), name='conversas'),
    path('chat/<str:email>/', ChatView.as_view(), name='chat'),
]
