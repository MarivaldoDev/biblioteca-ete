from django import forms
from django.core.exceptions import ValidationError
from .models import UserStandard, Emprestimo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = UserStandard
        fields = (
            'nome', 'matricula', 'curso', 'email',
            'turma', 'imagem'
        )

        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Seu nome', 'id': 'input'}),
            'matricula': forms.TextInput(attrs={'placeholder': 'Sua matricula', 'id': 'input2'}),
            'curso': forms.TextInput(attrs={'placeholder': 'Seu curso', 'id': 'input3'}),
            'email': forms.TextInput(attrs={'placeholder': 'Seu E-mail', 'id': 'input4'}),
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


class EmpreForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = (
            'portador', 'livro', 'categoria', 'data_emprestimo', 'data_devolucao'
        )

        widgets = {
            'portador': forms.TextInput(attrs={'placeholder': 'Nome do usuário...'}),
            'livro': forms.TextInput(attrs={'placeholder': 'Seu livro...'}),
            'categoria': forms.TextInput(attrs={'placeholder': 'Categoria do livro...'}),
            'data_emprestimo': forms.DateInput(attrs={'type': 'date', 'value': '{{ default_devolucao_date }}'}),
            'data_devolucao': forms.DateInput(attrs={'type': 'date', 'value': '{{ default_devolucao_date }}'}),
        }


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Nome do usuário...'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Senha...'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirme a senha...'}),
        }