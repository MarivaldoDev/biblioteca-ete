from django.shortcuts import render, redirect
from .models import Administrador
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