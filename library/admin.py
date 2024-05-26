from django.contrib import admin
from .models import Usuario, Categoria, Livro, Administrador

# Register your models here.
admin.site.register(Administrador)
admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Livro)