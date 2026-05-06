from django.shortcuts import render
from .models import *

# Esta é a tua página inicial
def home_page_view(request):
    return render(request, 'portfolio/home.html')

# Adiciona esta função que estava em falta:
def sobre_view(request):
    return render(request, 'portfolio/home.html') # Usa o template de apresentação

def licenciatura_view(request):
    context = {'licenciatura': Licenciatura.objects.first()}
    return render(request, 'portfolio/licenciatura.html', context)

def ucs_view(request):
    context = {'ucs': UnidadeCurricular.objects.all().order_by('ano', 'semestre')}
    return render(request, 'portfolio/ucs.html', context)

def projetos_view(request):
    context = {'projetos': Projeto.objects.all()}
    return render(request, 'portfolio/projetos.html', context)

def tecnologias_view(request):
    context = {'tecnologias': Tecnologia.objects.all().order_by('-preferencia')}
    return render(request, 'portfolio/tecnologias.html', context)

def tfc_view(request):
    context = {'tfcs': TFC.objects.all()}
    return render(request, 'portfolio/tfcs.html', context)

def competencias_view(request):
    return render(request, 'portfolio/competencias.html')

def formacoes_view(request):
    return render(request, 'portfolio/formacoes.html')

def makingof_view(request):
    return render(request, 'portfolio/makingof.html')