from django.shortcuts import render
from models import produto
from .form import produtoForm

def home(request):
    return render(request, 'winx_sistema_loja/index.html')

def cadastro(request):
    return render(request, 'winx_sistema_loja/cadastre-se.html')

def criar_lojinha(request):
    return render(request, 'winx_sistema_loja/criar-lojinha.html')

def user(request):
    return render(request, 'winx_sistema_loja/vendedor/user.html')
 
def dashboard(request):
    return render(request, 'winx_sistema_loja/vendedor/dashboard.html')

def pedidos(request):
    return render(request, 'winx_sistema_loja/vendedor/pedidos.html')

def notificacoes(request):
    return render(request, 'winx_sistema_loja/vendedor/notificacoes.html')

def visualizar_loja(request):
    return render(request, 'winx_sistema_loja/vendedor/visualizar_loja.html')

def estoque(request):
    return render(request, 'winx_sistema_loja/vendedor/estoque.html')


def novo_produto(request):
    data = {}
    form = produtoForm(request.Post or None)

    if form.is_valid():
        form.save()
    data['form'] = form
    return render(request, 'produto/form.html',data)
