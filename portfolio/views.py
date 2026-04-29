from django.shortcuts import render
from .models import Projeto, Tecnologia

def home_page_view(request):
    context = {
        'projetos': Projeto.objects.all(),
        'tecnologias': Tecnologia.objects.all(),
    }
    return render(request, 'portfolio/home.html', context)