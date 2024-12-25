from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import UserStandard, Emprestimo
from .forms import UserForm, EmpreForm, RegisterForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def first(request):
    return render(request, 'index.html')


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            nome = form.cleaned_data.get('username')
            messages.success(request, f'{nome} registrado com sucesso!')
            
            return redirect('login')

    context = {
        'form': form
    }

    return render(request, 'register.html', context)


def criar_usuario(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        
        context = {
            'form': form
        }

        if form.is_valid():
            if UserStandard.objects.filter(matricula=form.cleaned_data['matricula']).exists():
                messages.error(request, 'Já existe um usuário com essa matrícula!')
                return render(request, 'cadastrar.html', context)
            
            elif UserStandard.objects.filter(email=form.cleaned_data['email']).exists():
                messages.error(request, 'Já existe um usuário com esse email!')
                return render(request, 'cadastrar.html', context)
            
            else:
                form.save()
                messages.success(request, f'Usuário {form.cleaned_data['nome']} cadastrado com sucesso!')
                return redirect('first')
    
        return render(request, 'cadastrar.html', context)
    
    context = {
        'form': UserForm()
    }

    return render(request, 'cadastrar.html', context)


def listar(request):
    usuarios = UserStandard.objects.all()
    # print(usuarios)

    context = {
        'usuarios': usuarios
    }

    return render(request, 'listar_cadastros.html', context)


def search(request):
    search_value = request.GET.get('q', '').strip()
    search_type = request.GET.get('type', 'usuarios') 

    if search_value == '':
        if search_type == 'usuarios':
            return redirect('listar_usuarios')
        elif search_type == 'emprestimos':
            return redirect('listar_emprestimos')

    if search_type == 'usuarios':
        results = UserStandard.objects.filter(
            Q(nome__icontains=search_value) |
            Q(matricula__icontains=search_value) |
            Q(turma__icontains=search_value) |
            Q(email__icontains=search_value)
        )
        template = 'listar_cadastros.html'
        context_key = 'usuarios'

    elif search_type == 'emprestimos':
        results = Emprestimo.objects.filter(
            Q(portador__nome__icontains=search_value) |
            Q(livro__icontains=search_value) |
            Q(categoria__icontains=search_value)
        )
        template = 'listar_emprestimos.html'
        context_key = 'emprestimos'

    else:
        return HttpResponse("Tipo de busca inválido", status=400)

    context = {
        context_key: results
    }

    return render(request, template, context)



def emprestimos(request):
    if request.method == 'POST':
        form = EmpreForm(request.POST)

        if form.is_valid():
            form.save()
            print('foi')
            return redirect('emprestimos')
        else:
            print(form.errors)
        
        usuarios = UserStandard.objects.all()
        
        return render(request, 'emprestimos.html', context={'usuarios': usuarios, 'form': form})
    
    usuarios = UserStandard.objects.all()
    return render(request, 'emprestimos.html', context={'usuarios': usuarios, 'form': EmpreForm()})


def listar_emprestimo(request):
    emprestimos = Emprestimo.objects.all()
    
    return render(request, 'listar_emprestimos.html', context={'emprestimos': emprestimos})


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Login efetuado com sucesso!')
            return redirect('first')
      
        messages.error(request, 'Usuário ou senha inválidos!')

    context = {
        'form': form
    }
    
    return render(request, 'login.html', context)


def logout_view(request):
    auth.logout(request)
    
    return redirect('login')