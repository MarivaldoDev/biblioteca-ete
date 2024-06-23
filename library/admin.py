from django.contrib import admin
from .models import Administrator, User, Emprestimo

# Register your models here.
admin.site.register(Administrator)
admin.site.register(User)
admin.site.register(Emprestimo)