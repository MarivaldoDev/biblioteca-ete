from django import forms
from .models import Administrador


class AdmForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ('usuario', 'senha')