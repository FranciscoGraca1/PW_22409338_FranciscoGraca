from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegistoForm, MagicLinkForm
from .models import MagicToken


# ── Registo ──────────────────────────────────────────────────────────────────
def registo_view(request):
    if request.method == 'POST':
        form = RegistoForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Adiciona automaticamente ao grupo 'autores'
            grupo, _ = Group.objects.get_or_create(name='autores')
            user.groups.add(grupo)
            login(request, user)
            return redirect('portfolio:home')
    else:
        form = RegistoForm()
    return render(request, 'accounts/registo.html', {'form': form})


# ── Login por senha ───────────────────────────────────────────────────────────
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(request.GET.get('next', 'portfolio:home'))
    else:
        form = AuthenticationForm()
    magic_form = MagicLinkForm()
    return render(request, 'accounts/login.html', {'form': form, 'magic_form': magic_form})


# ── Logout ────────────────────────────────────────────────────────────────────
def logout_view(request):
    logout(request)
    return redirect('portfolio:home')


# ── Magic Link — pedir link ───────────────────────────────────────────────────
def magic_link_request_view(request):
    if request.method == 'POST':
        form = MagicLinkForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Cria token (independentemente de o utilizador existir — não revelamos isso)
            token_obj = MagicToken.objects.create(email=email)
            link = request.build_absolute_uri(f'/accounts/magic/{token_obj.token}/')
            send_mail(
                subject='O teu link de acesso',
                message=f'Clica no link para entrar (válido 15 minutos):\n\n{link}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
            )
            return render(request, 'accounts/magic_link_enviado.html', {'email': email})
    else:
        form = MagicLinkForm()
    return render(request, 'accounts/login.html', {'form': AuthenticationForm(), 'magic_form': form})


# ── Magic Link — verificar token ──────────────────────────────────────────────
def magic_link_verify_view(request, token):
    token_obj = get_object_or_404(MagicToken, token=token)

    if not token_obj.is_valido():
        return render(request, 'accounts/magic_link_invalido.html')

    # Encontra ou cria utilizador com esse email
    email = token_obj.email
    user, created = User.objects.get_or_create(
        email=email,
        defaults={'username': email.split('@')[0]}
    )
    if created:
        grupo, _ = Group.objects.get_or_create(name='autores')
        user.groups.add(grupo)

    # Marca o token como usado
    token_obj.usado = True
    token_obj.save()

    # Log in sem password (backend explícito)
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)
    return redirect('portfolio:home')