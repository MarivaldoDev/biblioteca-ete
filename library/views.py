from django.shortcuts import render, redirect
from .models import Administrador, Usuario
from .forms import AdmForm

# Create your views here.
def first(request):
    return render(request, 'first.html')


def criar(request):
    if request.method == 'POST':
        context = {
            'form': AdmForm(request.POST)
        }
        # usuario = request.POST.get('usuario')
        # senha = request.POST.get('senha')
        
        # adm = Administrador(usuario=usuario, senha=senha) 
        # adm.save()

        return render(request, 'criar_adm.html', context)
    
    context = {
        'form': AdmForm()
    }

    return render(request, 'criar_adm.html', context)

def criar_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        matricula = request.POST.get('matricula')
        curso = request.POST.get('curso')
        turma = request.POST.get('turma')
        data_criacao = request.POST.get('data')

        aluno = Usuario(nome=nome, matricula=matricula, curso=curso, turma=turma, data_criacao=data_criacao)
        aluno.save()
        print('foi')

        return render(request, 'usuario.html')

    return render(request, 'usuario.html')