from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Administrator, User, Emprestimo
from .forms import UserForm, EmpreForm


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
    
        return render(request, 'cadastrar.html', context)
    
    context = {
        'form': UserForm()
    }

    return render(request, 'cadastrar.html', context)


def listar(request):
    usuarios = User.objects.all()
    # print(usuarios)

    context = {
        'usuarios': usuarios
    }

    return render(request, 'listar_cadastros.html', context)


def search(request):
    search_value = request.GET.get('q', '').strip()
    print(search_value)

    if search_value == '':
        return redirect('listar_usuarios')

    usuarios = User.objects.filter(
        Q(nome__icontains=search_value) |
        Q(matricula__icontains=search_value) |
        Q(turma__icontains=search_value) |
        Q(email__icontains=search_value)
    )

    context = {
        'usuarios': usuarios
    }

    return render(request, 'listar_cadastros.html', context)


def emprestimos(request):
    if request.method == 'POST':
        form = EmpreForm(request.POST)

        if form.is_valid():
            form.save()
            print('foi')
            return redirect('emprestimos')
        else:
            print(form.errors)
        
        usuarios = User.objects.all()
        
        return render(request, 'emprestimos.html', context={'usuarios': usuarios, 'form': form})
    
    usuarios = User.objects.all()
    return render(request, 'emprestimos.html', context={'usuarios': usuarios, 'form': EmpreForm()})


def listar_emprestimo(request):
    emprestimos = Emprestimo.objects.all()
    
    return render(request, 'listar_emprestimos.html', context={'emprestimos': emprestimos})
