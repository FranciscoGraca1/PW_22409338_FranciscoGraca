from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# --- Listagens ---
def home_page_view(request):
    return render(request, 'portfolio/home.html')

def sobre_view(request):
    return render(request, 'portfolio/home.html')

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


# --- CRUD Projetos ---
def projeto_novo_view(request):
    form = ProjetoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:projetos')
    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Novo Projeto'})

def projeto_edita_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    form = ProjetoForm(request.POST or None, request.FILES or None, instance=projeto)
    if form.is_valid():
        form.save()
        return redirect('portfolio:projetos')
    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Editar Projeto'})

def projeto_apaga_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    projeto.delete()
    return redirect('portfolio:projetos')


# --- CRUD Tecnologias ---
def tecnologia_novo_view(request):
    form = TecnologiaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:tecnologias')
    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Nova Tecnologia'})

def tecnologia_edita_view(request, tecnologia_id):
    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)
    form = TecnologiaForm(request.POST or None, request.FILES or None, instance=tecnologia)
    if form.is_valid():
        form.save()
        return redirect('portfolio:tecnologias')
    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Editar Tecnologia'})

def tecnologia_apaga_view(request, tecnologia_id):
    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)
    tecnologia.delete()
    return redirect('portfolio:tecnologias')


# --- CRUD Competências ---
def competencia_novo_view(request):
    form = CompetenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:competencias')
    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Nova Competência'})

def competencia_edita_view(request, competencia_id):
    competencia = get_object_or_404(Competencia, id=competencia_id)
    form = CompetenciaForm(request.POST or None, instance=competencia)
    if form.is_valid():
        form.save()
        return redirect('portfolio:competencias')
    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Editar Competência'})

def competencia_apaga_view(request, competencia_id):
    competencia = get_object_or_404(Competencia, id=competencia_id)
    competencia.delete()
    return redirect('portfolio:competencias')


# --- CRUD Formações ---
def formacao_novo_view(request):
    form = FormacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:formacoes')
    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Nova Formação'})

def formacao_edita_view(request, formacao_id):
    formacao = get_object_or_404(Formacao, id=formacao_id)
    form = FormacaoForm(request.POST or None, instance=formacao)
    if form.is_valid():
        form.save()
        return redirect('portfolio:formacoes')
    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Editar Formação'})

def formacao_apaga_view(request, formacao_id):
    formacao = get_object_or_404(Formacao, id=formacao_id)
    formacao.delete()
    return redirect('portfolio:formacoes')