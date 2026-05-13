from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Artigo, Comentario
from .forms import ArtigoForm, ComentarioForm


def _is_autor(user):
    return user.is_authenticated and user.groups.filter(name='autores').exists()


def lista_view(request):
    artigos = Artigo.objects.all().order_by('-data_criacao')
    return render(request, 'artigos/lista.html', {'artigos': artigos})


def detalhe_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    comentarios = artigo.comentarios.all().order_by('data')
    form_comentario = ComentarioForm()

    if request.method == 'POST' and request.user.is_authenticated:
        form_comentario = ComentarioForm(request.POST)
        if form_comentario.is_valid():
            c = form_comentario.save(commit=False)
            c.artigo = artigo
            c.autor = request.user
            c.save()
            return redirect('artigos:detalhe', artigo_id=artigo.id)

    ja_deu_like = request.user.is_authenticated and artigo.likes.filter(id=request.user.id).exists()

    return render(request, 'artigos/detalhe.html', {
        'artigo': artigo,
        'comentarios': comentarios,
        'form_comentario': form_comentario,
        'ja_deu_like': ja_deu_like,
    })


@login_required
def novo_view(request):
    if not _is_autor(request.user):
        return redirect('artigos:lista')
    form = ArtigoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        artigo = form.save(commit=False)
        artigo.autor = request.user
        artigo.save()
        return redirect('artigos:lista')
    return render(request, 'artigos/form_artigo.html', {'form': form, 'titulo': 'Novo Artigo'})


@login_required
def editar_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    # Só o autor do artigo pode editar
    if artigo.autor != request.user:
        return redirect('artigos:lista')
    form = ArtigoForm(request.POST or None, request.FILES or None, instance=artigo)
    if form.is_valid():
        form.save()
        return redirect('artigos:detalhe', artigo_id=artigo.id)
    return render(request, 'artigos/form_artigo.html', {'form': form, 'titulo': 'Editar Artigo'})


@login_required
def apagar_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    if artigo.autor == request.user:
        artigo.delete()
    return redirect('artigos:lista')


@login_required
def like_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    if artigo.likes.filter(id=request.user.id).exists():
        artigo.likes.remove(request.user)
    else:
        artigo.likes.add(request.user)
    return redirect('artigos:detalhe', artigo_id=artigo.id)
