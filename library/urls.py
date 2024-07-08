from django.urls import path
from . import views


urlpatterns = [
    path('', views.first, name='first'),
    path('criar_usuario/', views.criar_usuario, name='criar_usuario'),
    path('listar_usuarios/', views.listar, name='listar_usuarios'),
    path('emprestimos/', views.emprestimo, name='emprestimos'),
]