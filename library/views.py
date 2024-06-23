from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Administrator, User, Emprestimo
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
    usuarios = User.objects.all()
    # print(usuarios)

    context = {
        'usuarios': usuarios
    }

    return render(request, 'listar.html', context)


def emprestimo(request):
    emprestimos = Emprestimo.objects.all()

    for emprestimo in emprestimos:
        if emprestimo.fim_emprestimo:
            print(f"Chegou a hora de devolver o livro: {emprestimo.livro}")
        else:     
            print(f'Pode usar o livro tranquilamente, você ainda tem: {emprestimo.data_devolucao - emprestimo.data_emprestimo} dias')
    return HttpResponse('estou no emprestimo')