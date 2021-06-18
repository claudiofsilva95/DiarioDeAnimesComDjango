from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        senha2 = request.POST['senha2']
        if not nome.strip() or not email.strip():
            messages.error(request, 'Nenhum dos campos podem ficar em branco!')
            return redirect('cadastro')
        if senha != senha2:
            messages.error(request, 'As senhas não correspondem')
            return redirect('cadastro')
        if len(senha) < 8:
            messages.error(request, 'A senha deve conter no mínimo 8 caracteres')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Este email já está cadastrado')
            return redirect('cadastro')
        else:
            user = User.objects.create_user(username=email, email=email, password=senha, first_name=nome)
            user.save()
            messages.success(request, 'Usuário criado com sucesso')
            return redirect('login')
    return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if not email.strip() or not senha.strip():
            messages.error(request, 'Nenhum dos campos podem ficar em branco')
            return redirect('login')
        user = auth.authenticate(request, username=email, password=senha)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        messages.error(request, 'Senha ou email incorreto')
    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')