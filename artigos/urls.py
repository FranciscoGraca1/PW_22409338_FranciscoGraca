from django.urls import path
from . import views

app_name = 'artigos'

urlpatterns = [
    path('', views.lista_view, name='lista'),
    path('<int:artigo_id>/', views.detalhe_view, name='detalhe'),
    path('novo/', views.novo_view, name='novo'),
    path('<int:artigo_id>/editar/', views.editar_view, name='editar'),
    path('<int:artigo_id>/apagar/', views.apagar_view, name='apagar'),
    path('<int:artigo_id>/like/', views.like_view, name='like'),
]
