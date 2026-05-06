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
]