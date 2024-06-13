from django.shortcuts import render, redirect
from .models import Administrador, Usuario
from .forms import UserForm

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
    usuarios = Usuario.objects.all()
    print(usuarios)

    context = {
        'usuarios': usuarios
    }

    return render(request, 'listar.html', context)