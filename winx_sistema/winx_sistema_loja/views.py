from django.shortcuts import render
from .models import loja
from .form import lojaForm
from models import produto
from .form import produtoForm

def home(request):
    return render(request, 'winx_sistema_loja/index.html')

def cadastro(request):
    return render(request, 'winx_sistema_loja/cadastrese.html')

def criar_lojinha(request):
    return render(request, 'winx_sistema_loja/criar_lojinha.html')

def user(request):
    return render(request, 'winx_sistema_loja/vendedor/user.html')
 
def produtos(request):
    return render(request, 'winx_sistema_loja/vendedor/produtos.html')

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

def nova_loja(request):
    data_loja = {}
    form = lojaForm(request.POST or None)

    if form.is_valid():
        form.save()
         
    data_loja['form'] = form
    return render(request, 'loj/form.html', data_loja)