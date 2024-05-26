from django.shortcuts import render, redirect
from .models import Administrador

# Create your views here.
def first(request):
    return render(request, 'first.html')


def criar(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        
        adm = Administrador(usuario=usuario, senha=senha) 
        adm.save()

        return redirect('/')

    return render(request, 'criar.html')