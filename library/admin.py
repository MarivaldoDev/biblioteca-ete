from django.contrib import admin

from .models import Emprestimo, UserStandard

# Register your models here.
admin.site.register(UserStandard)
admin.site.register(Emprestimo)
