from django import forms
from django.core.exceptions import ValidationError
from .models import Administrador, Usuario


class UserForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = (
            'nome', 'matricula', 'curso', 'turma',
            'data_criacao', 'imagem'
        )

        widgets = {
            'data_criacao': forms.DateInput(attrs={'type': 'date'}),
            'imagem': forms.FileInput(attrs={'class': 'file'}),
        }

    # def clean(self):
    #     # cleaned_data = self.cleaned_data

    #     self.add_error(
    #         'nome',
    #         ValidationError(
    #             'Erro', code='invalido'
    #         )
    #     )

    #     return super().clean()

class AdmForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ('usuario', 'senha')