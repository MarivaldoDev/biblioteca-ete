from django import forms
from django.core.exceptions import ValidationError
from .models import Administrator, User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'nome', 'matricula', 'curso', 'turma',
            'data_criacao', 'imagem'
        )

        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Seu nome', 'id': 'input'}),
            'matricula': forms.TextInput(attrs={'placeholder': 'Sua matricula', 'id': 'input2'}),
            'curso': forms.TextInput(attrs={'placeholder': 'Seu curso', 'id': 'input3'}),
            'data_criacao': forms.DateInput(attrs={'type': 'date', 'id': 'input4'}),
            'imagem': forms.FileInput(attrs={'class': 'file', 'placeholder': 'Adicione uma imagem', 'id': 'input5'}),
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
        model = Administrator
        fields = ('usuario', 'senha')