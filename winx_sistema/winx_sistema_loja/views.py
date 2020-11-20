from django.shortcuts import render

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
