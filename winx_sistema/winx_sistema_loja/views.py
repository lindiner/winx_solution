from django.shortcuts import render, redirect
from .models import loja, produto, usuario
from .form import lojaForm 
from .form.produtoForm import ProdutoForm
from .form.usuarioForm import UsuarioForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    return render(request, 'winx_sistema_loja/index.html')

def cadastro(request):

    if request.method == 'POST':
        form = UsuarioForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('winx_sistema-cria_lojinha'))

    else: 
        form = UsuarioForm()
    
    
    return render(request, 'winx_sistema_loja/cadastro.html', {'form':form})


def criar_lojinha(request):
    return render(request, 'winx_sistema_loja/criar_lojinha.html')

def user(request):
    return render(request, 'winx_sistema_loja/vendedor/user.html')
 
def produtos(request):
    
    if request.method == 'POST':
        form = ProdutoForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('winx_sistema-estoque'))

    else: 
        form = ProdutoForm()
    
    
    return render(request, 'winx_sistema_loja/vendedor/produtos.html', {'form':form})


def pedidos(request):
    return render(request, 'winx_sistema_loja/vendedor/pedidos.html')

def notificacoes(request):
    return render(request, 'winx_sistema_loja/vendedor/notificacoes.html')

def loja(request):
    return render(request, 'winx_sistema_loja/vendedor/loja.html')

def estoque(request):
    return render(request, 'winx_sistema_loja/vendedor/estoque.html')

def novo_produto(request):
    data = {}
    form = produtoForm(request.Post or None)

    if form.is_valid():
        form.save()
    data['form'] = form
    return render(request, 'produto/form.html',data)

def nova_loja(request):
    data_loja = {}
    form = lojaForm(request.POST or None)

    if form.is_valid():
        form.save()
         
    data_loja['form'] = form
    return render(request, 'loja/form.html', data_loja)

def novo_login(request):
    data_login = {}
    form = usuarioLoginForm(request.POST or None)

    if form.is_valid():
        form.save()
         
    data_login['form'] = form
    return render(request, 'loja/form.html', data_login)
    