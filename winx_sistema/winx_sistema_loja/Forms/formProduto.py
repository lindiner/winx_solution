from django.forms import ModelForm
from.models import produto

class produtoForm(ModelForm):
    class Meta:
        model = produto
        fields = ['idProduto','name','precoProduto','codigoProduto','quantidadeEstoque','corProduto','tamanho']
        
