from django.shortcuts import render
from .models import Curso, Aluno, Professor

# View de Cursos (já deves ter)
def cursos_view(request):
    cursos = Curso.objects.select_related('professor').prefetch_related('alunos').all()
    return render(request, 'escola/cursos.html', {'cursos': cursos})

# NOVA: View de Alunos
def alunos_view(request):
    alunos = Aluno.objects.prefetch_related('cursos').all()
    return render(request, 'escola/alunos.html', {'alunos': alunos})

# NOVA: View de Professores
def professores_view(request):
    professores = Professor.objects.prefetch_related('cursos').all()
    return render(request, 'escola/professores.html', {'professores': professores})