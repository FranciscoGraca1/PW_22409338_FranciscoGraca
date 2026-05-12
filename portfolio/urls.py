from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('sobre/', views.sobre_view, name='sobre'), # Agora a view já existe
    path('licenciatura/', views.licenciatura_view, name='licenciatura'),
    path('ucs/', views.ucs_view, name='ucs'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('tfcs/', views.tfc_view, name='tfc'),
    path('makingof/', views.makingof_view, name='makingof'),
    path('projeto/novo/', views.projeto_novo_view, name='projeto_novo'),
    path('projeto/edita/<int:projeto_id>/', views.projeto_edita_view, name='projeto_edita'),
    path('projeto/apaga/<int:projeto_id>/', views.projeto_apaga_view, name='projeto_apaga'),
    path('tecnologia/novo/', views.tecnologia_novo_view, name='tecnologia_novo'),
    path('tecnologia/edita/<int:tecnologia_id>/', views.tecnologia_edita_view, name='tecnologia_edita'),
    path('tecnologia/apaga/<int:tecnologia_id>/', views.tecnologia_apaga_view, name='tecnologia_apaga'),
]