from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistoForm


def registo_view(request):
    if request.method == 'POST':
        form = RegistoForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # --- Lógica de Autores ---
            # Procura o grupo 'autores'. Se não existir, ele cria-o.
            grupo, created = Group.objects.get_or_create(name='autores')
            # Adiciona o utilizador recém-criado ao grupo
            user.groups.add(grupo)
            
            # Faz login automático após o registo
            login(request, user)
            
            # Redireciona para a página inicial do portfólio
            return redirect('portfolio:home')
    else:
        form = RegistoForm()
    
    return render(request, 'accounts/registo.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('portfolio:home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('portfolio:home')