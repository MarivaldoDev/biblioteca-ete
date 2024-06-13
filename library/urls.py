from django.urls import path
from . import views

urlpatterns = [
    path('', views.first, name='first'),
    path('usuario/', views.criar_usuario, name='criar_usuario'),
    path('listar/', views.listar, name='listar_usuarios'),
]