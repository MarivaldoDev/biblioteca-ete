from django.http import HttpResponse
from django.utils import timezone
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Administrator, User, Emprestimo
from .forms import UserForm
from datetime import date

# Create your views here.
def first(request):
    return render(request, 'index.html')


def criar_usuario(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        
        context = {
            'form': form
        }

        if form.is_valid():
            form.save()
            return redirect('criar_usuario')
    
        return render(request, 'pag1.html', context)
    
    context = {
        'form': UserForm()
    }

    return render(request, 'pag1.html', context)


def listar(request):
    usuarios = User.objects.all()
    # print(usuarios)

    context = {
        'usuarios': usuarios
    }

    return render(request, 'listar_cadastros.html', context)


def emprestimo(request):
    emprestimos = Emprestimo.objects.all()

    for emprestimo in emprestimos:
        if emprestimo.fim_emprestimo:
            send_mail(
                subject='Hora de devolver!', 
                message=f'Olá {emprestimo.portador}, você precisa devolver ou renovar o empréstimo do livro {emprestimo.livro} à biblioteca.',
                from_email='testesdepython2@gmail.com',
                recipient_list=[emprestimo.email]
            )
    return render(request, 'emprestimos.html', context={'emprestimos': emprestimos})
