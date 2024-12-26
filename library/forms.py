from django import forms
from django.core.exceptions import ValidationError
from .models import UserStandard, Emprestimo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
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

class RegisterUpdateForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Senha",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )
    
    password2 = forms.CharField(
        label="Confirmar senha",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Use the same password as before.',
        required=False,
    )
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


        def save(self, commit=True):
            cleaned_data = self.cleaned_data
            user = super().save(commit=False)
            password = cleaned_data.get('password1')
            
            if password:
                user.set_password(password)
            
            if commit:
                user.save()
            
            return user
        

        def clean(self):
            password1 = self.cleaned_data.get('password1')
            password2 = self.cleaned_data.get('password2')
            
            if password1 or password2:
                if password1 != password2:
                    self.add_error(
                        'password2',
                        ValidationError('Senhas não batem')
                    )
            
            return super().clean()
        

        def clean_password1(self):
            password1 = self.cleaned_data.get('password1')
            
            if password1:
                try:
                    password_validation.validate_password(password1)
                except ValidationError as errors:
                    self.add_error(
                        'password1',
                        ValidationError(errors)
                    )
            
            return password1