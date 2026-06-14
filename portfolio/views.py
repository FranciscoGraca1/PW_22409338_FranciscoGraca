import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# ── Páginas principais ────────────────────────────────────────────────────────

def landing_view(request):
    return render(request, 'portfolio/landing.html')

def home_page_view(request):
    return render(request, 'portfolio/home.html')

def sobre_view(request):
    apps = [
        {'nome': 'portfolio', 'descricao': 'Percurso académico, projetos, tecnologias, competências e formações.'},
        {'nome': 'artigos', 'descricao': 'Publicação de artigos técnicos com comentários e avaliações.'},
        {'nome': 'accounts', 'descricao': 'Autenticação por senha, magic link e OAuth (Google).'},
        {'nome': 'boxe', 'descricao': 'API RESTful de boxe com lutadores, combates e títulos. Protegida por API Key.'},
    ]
    return render(request, 'portfolio/sobre.html', {'apps': apps})

def videos_view(request):
    return render(request, 'portfolio/videos.html')

def licenciatura_view(request):
    context = {'licenciatura': Licenciatura.objects.first()}
    return render(request, 'portfolio/licenciatura.html', context)

def ucs_view(request):
    context = {'ucs': UnidadeCurricular.objects.all().order_by('ano', 'semestre')}
    return render(request, 'portfolio/ucs.html', context)

def docentes_view(request):
    context = {'docentes': Docente.objects.all()}
    return render(request, 'portfolio/docentes.html', context)

def projetos_view(request):
    context = {'projetos': Projeto.objects.all()}
    return render(request, 'portfolio/projetos.html', context)

def tecnologias_view(request):
    context = {'tecnologias': Tecnologia.objects.all().order_by('-preferencia')}
    return render(request, 'portfolio/tecnologias.html', context)

def tfc_view(request):
    context = {'tfcs': TFC.objects.all()}
    return render(request, 'portfolio/tfc.html', context)

def competencias_view(request):
    context = {'competencias': Competencia.objects.all()}
    return render(request, 'portfolio/competencias.html', context)

def formacoes_view(request):
    context = {'formacoes': Formacao.objects.all()}
    return render(request, 'portfolio/formacoes.html', context)

def makingof_view(request):
    return render(request, 'portfolio/makingof.html')

def boxe_view(request):
    categorias = [
        'heavyweight', 'cruiserweight', 'light-heavyweight',
        'super-middleweight', 'middleweight', 'welterweight',
        'lightweight', 'featherweight', 'bantamweight', 'flyweight'
    ]
    categoria = request.GET.get('categoria', 'heavyweight')
    try:
        response = requests.get(
            f'https://openboxing.org/api/{categoria}/bouts.json',
            verify=False
        )
        combates = response.json() if response.status_code == 200 else []
    except:
        combates = []
    return render(request, 'portfolio/boxe.html', {
        'combates': combates,
        'categoria': categoria,
        'categorias': categorias
    })

# ── CRUD Projetos ─────────────────────────────────────────────────────────────

@login_required
def projeto_novo_view(request):
    form = ProjetoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:projetos')
    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Novo Projeto'})

@login_required
def projeto_edita_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    form = ProjetoForm(request.POST or None, request.FILES or None, instance=projeto)
    if form.is_valid():
        form.save()
        return redirect('portfolio:projetos')
    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Editar Projeto'})

@login_required
def projeto_apaga_view(request, projeto_id):
    get_object_or_404(Projeto, id=projeto_id).delete()
    return redirect('portfolio:projetos')

# ── CRUD Tecnologias ──────────────────────────────────────────────────────────

@login_required
def tecnologia_novo_view(request):
    form = TecnologiaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:tecnologias')
    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Nova Tecnologia'})

@login_required
def tecnologia_edita_view(request, tecnologia_id):
    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)
    form = TecnologiaForm(request.POST or None, request.FILES or None, instance=tecnologia)
    if form.is_valid():
        form.save()
        return redirect('portfolio:tecnologias')
    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Editar Tecnologia'})

@login_required
def tecnologia_apaga_view(request, tecnologia_id):
    get_object_or_404(Tecnologia, id=tecnologia_id).delete()
    return redirect('portfolio:tecnologias')

# ── CRUD Competências ─────────────────────────────────────────────────────────

@login_required
def competencia_novo_view(request):
    form = CompetenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:competencias')
    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Nova Competência'})

@login_required
def competencia_edita_view(request, competencia_id):
    competencia = get_object_or_404(Competencia, id=competencia_id)
    form = CompetenciaForm(request.POST or None, instance=competencia)
    if form.is_valid():
        form.save()
        return redirect('portfolio:competencias')
    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Editar Competência'})

@login_required
def competencia_apaga_view(request, competencia_id):
    get_object_or_404(Competencia, id=competencia_id).delete()
    return redirect('portfolio:competencias')

# ── CRUD Formações ────────────────────────────────────────────────────────────

@login_required
def formacao_novo_view(request):
    form = FormacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:formacoes')
    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Nova Formação'})

@login_required
def formacao_edita_view(request, formacao_id):
    formacao = get_object_or_404(Formacao, id=formacao_id)
    form = FormacaoForm(request.POST or None, instance=formacao)
    if form.is_valid():
        form.save()
        return redirect('portfolio:formacoes')
    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Editar Formação'})

@login_required
def formacao_apaga_view(request, formacao_id):
    get_object_or_404(Formacao, id=formacao_id).delete()
    return redirect('portfolio:formacoes')
