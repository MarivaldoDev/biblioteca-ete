from django.db import models
from datetime import date
from django.utils import timezone

# Create your models here.


class Administrator(models.Model):
    class Meta:
        verbose_name_plural = 'administrators'
    
    usuario = models.CharField(max_length=20)
    senha = models.CharField(max_length=8)


class User(models.Model):
    class Meta:
        verbose_name_plural = 'users'
    
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=7)
    curso = models.CharField(max_length=40)
    turma = models.CharField(max_length=10)
    data_criacao = models.DateField(default=date.today().strftime('%d/%m/%Y'))
    imagem = models.ImageField(blank=True, upload_to='imagem_cadastro/%Y/%m/')

    def __str__(self) -> str:
        return f'{self.nome}'


class Emprestimo(models.Model):
    portador = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=150)
    livro = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50, blank=True)
    data_emprestimo = models.DateField(default=date.today().strftime('%d/%m/%Y'))
    data_devolucao = models.DateField(default=date.today().strftime('%d/%m/%Y'))

    @property
    def fim_emprestimo(self):
        return self.data_devolucao <= timezone.now().date()
    
    def __str__(self) -> str:
        return f'Empréstimo - {self.portador}'