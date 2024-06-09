from django.db import models
from datetime import date

# Create your models here.


class Administrador(models.Model):
    usuario = models.CharField(max_length=20)
    senha = models.CharField(max_length=8)


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=7)
    curso = models.CharField(max_length=40)
    turma = models.CharField(max_length=10)
    data_criacao = models.DateField(default=date.today().strftime('%d/%m/%Y'))
    imagem = models.ImageField(blank=True, upload_to='imagem_cadastro/%Y/%m/')

    def __str__(self) -> str:
        return f'{self.nome}'


class Categoria(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name
 

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    data_emprestimo = models.DateField(blank=True, null=True)
    data_devolucao = models.DateField(blank=True, null=True)