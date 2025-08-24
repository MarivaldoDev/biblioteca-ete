from django.urls import path

from . import views

urlpatterns = [
    path("", views.first, name="first"),
    path("studant/create/user/", views.criar_usuario, name="criar_usuario"),
    path("studant/list/user/", views.listar, name="listar_usuarios"),
    path("studant/update/user/<int:id>/", views.update, name="update"),
    path("studant/delete/user/<int:id>/", views.excluir, name="excluir"),
    path("studant/search", views.search, name="search"),
    path(
        "studant/search/user/",
        views.search,
        {"type": "usuarios"},
        name="search_usuarios",
    ),
    path(
        "studant/search/loan/",
        views.search,
        {"type": "emprestimos"},
        name="search_emprestimos",
    ),
    path("studant/loan/", views.emprestimos, name="emprestimos"),
    path("studant/list/loan/", views.listar_emprestimo, name="listar_emprestimos"),
    path("user/create", views.register, name="register"),
    path("user/login", views.login_view, name="login"),
    path("user/logout", views.logout_view, name="logout"),
    path("user/update", views.register_update, name="register_update"),
]
