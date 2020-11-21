from django.shortcuts import render, redirect
from .models import loja, produto, usuario
from .form.lojaForm  import LojaForm
from .form.produtoForm import ProdutoForm
from .form.usuarioForm import UsuarioForm
from .form.usuarioForm import UsuarioLoginForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    if request.method == 'POST':
        form = UsuarioLoginForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('winx_sistema-produtos'))
    else:
        form = UsuarioLoginForm()
    return render(request, 'winx_sistema_loja/index.html', {'form':form})

def cadastro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('winx_sistema-criar_lojinha'))
    else: 
        form = UsuarioForm() 
    return render(request, 'winx_sistema_loja/cadastro.html', {'form':form})


def criar_lojinha(request):
    if request.method == 'POST':
        form = LojaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('winx_sistema-produtos'))
    else: 
        form = LojaForm()
    return render(request, 'winx_sistema_loja/criar_lojinha.html',  {'form':form})

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

def loja(request,id):
    if request.method == 'POST':
        pi = produto.objects.get(pk=id)
        fm = ProdutoForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = ProdutoForm(instance=pi)

    return render(request, 'winx_sistema_loja/vendedor/loja.html', {'form':form})


def estoque(request):
    produtos = produto.objects.all()

    return render(request, 'winx_sistema_loja/vendedor/estoque.html', {'produtos':produtos})
