from django.shortcuts import render
from .models import loja
from .form import lojaForm
from .models import produto
from .form import produtoForm
from .models import usuario
from .form import usuarioForm

def home(request):
    return render(request, 'winx_sistema_loja/index.html')

def cadastro(request):
    return render(request, 'winx_sistema_loja/cadastro.html')

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
    return render(request, 'loj/form.html', data_loja)

def novo_vendedor(request):
    data_usuario = {}
    form = usuarioForm(request.POST or None)

    if form.is_valid():
        form.save()
         
    data_usuario['form'] = form
    return render(request, 'loj/form.html', data_usuario)


def novo_login(request):
    data_login = {}
    form = usuarioLoginForm(request.POST or None)

    if form.is_valid():
        form.save()
         
    data_login['form'] = form
    return render(request, 'loj/form.html', data_login)

def update(request, pk):
    data = {}
    produto = produto.object.get(pk=pk)
    form = produtoForm(request.POST or None, instance = produto)
    
    if form.is_valid():
        form.save()
    data['form'] = form
    return render(request, 'produto/form.html',data)


def update(request, pk):
    data_usuario = {}
    usuario = usuario.object.get(pk=pk)
    form = usuarioForm(request.POST or None, instance = usuario)

    if form.is_valid():
        form.save()
         
    data_usuario['form'] = form
    return render(request, 'loj/form.html', data_usuario)