from django.urls import path
from . import views  # Isto importa o ficheiro views.py que está na mesma pasta

app_name = 'escola'

urlpatterns = [
    path('cursos/', views.cursos_view, name='cursos'),
]