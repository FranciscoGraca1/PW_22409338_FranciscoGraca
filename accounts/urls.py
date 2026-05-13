from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registo/', views.registo_view, name='registo'),
    path('magic/', views.magic_link_request_view, name='magic_link_request'),
    path('magic/<uuid:token>/', views.magic_link_verify_view, name='magic_link_verify'),
]
