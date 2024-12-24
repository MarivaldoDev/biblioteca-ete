from django.urls import path
from . import views


urlpatterns = [
    path('', views.first, name='first'),
    path('criar_usuario/', views.criar_usuario, name='criar_usuario'),
    path('listar_usuarios/', views.listar, name='listar_usuarios'),
    path('search', views.search, name='search'),
    path('search/usuarios/', views.search, {'type': 'usuarios'}, name='search_usuarios'),
    path('search/emprestimos/', views.search, {'type': 'emprestimos'}, name='search_emprestimos'),
    path('emprestimos/', views.emprestimos, name='emprestimos'),
    path('listar_emprestimos/', views.listar_emprestimo, name='listar_emprestimos'),
]