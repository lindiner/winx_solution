from django.forms import ModelForm
from winx_sistema_loja.models import produto

class produtoForm(ModelForm):
    class Meta:
        model = produto
        fields = ['name','precoProduto','codigoProduto','quantidadeEstoque','corProduto','tamanho']

  
        
