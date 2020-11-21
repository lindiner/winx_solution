from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='winx_sistema-home'),
    path('cadastro/', views.cadastro, name='winx_sistema-cadastro'),
    path('criar_lojinha/', views.criar_lojinha, name='winx_sistema-criar_lojinha'),
    path('user/', views.user, name='winx_sistema-user'),
    path('produtos/', views.produtos, name='winx_sistema-produtos'),
    path('pedidos/', views.pedidos, name='winx_sistema-pedidos'),
    path('notificacoes/', views.notificacoes, name='winx_sistema-notificacoes'),
    path('loja/', views.loja, name='winx_sistema-visualizar_loja'),
    path('estoque/', views.estoque, name='winx_sistema-estoque'),
    
]