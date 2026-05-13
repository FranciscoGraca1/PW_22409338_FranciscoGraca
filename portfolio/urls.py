from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    # --- Páginas principais ---
    path('', views.home_page_view, name='home'),
    path('sobre/', views.sobre_view, name='sobre'),
    path('licenciatura/', views.licenciatura_view, name='licenciatura'),
    path('ucs/', views.ucs_view, name='ucs'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('tfcs/', views.tfc_view, name='tfc'),
    path('competencias/', views.competencias_view, name='competencias'),
    path('formacoes/', views.formacoes_view, name='formacoes'),
    path('makingof/', views.makingof_view, name='makingof'),

    # --- CRUD Projetos ---
    path('projeto/novo/', views.projeto_novo_view, name='novo_projeto'),
    path('projeto/edita/<int:projeto_id>/', views.projeto_edita_view, name='editar_projeto'),
    path('projeto/apaga/<int:projeto_id>/', views.projeto_apaga_view, name='apagar_projeto'),

    # --- CRUD Tecnologias ---
    path('tecnologia/novo/', views.tecnologia_novo_view, name='nova_tecnologia'),
    path('tecnologia/edita/<int:tecnologia_id>/', views.tecnologia_edita_view, name='editar_tecnologia'),
    path('tecnologia/apaga/<int:tecnologia_id>/', views.tecnologia_apaga_view, name='apagar_tecnologia'),

    # --- CRUD Competências ---
    path('competencia/novo/', views.competencia_novo_view, name='nova_competencia'),
    path('competencia/edita/<int:competencia_id>/', views.competencia_edita_view, name='editar_competencia'),
    path('competencia/apaga/<int:competencia_id>/', views.competencia_apaga_view, name='apagar_competencia'),

    # --- CRUD Formações ---
    path('formacao/novo/', views.formacao_novo_view, name='nova_formacao'),
    path('formacao/edita/<int:formacao_id>/', views.formacao_edita_view, name='editar_formacao'),
    path('formacao/apaga/<int:formacao_id>/', views.formacao_apaga_view, name='apagar_formacao'),
]