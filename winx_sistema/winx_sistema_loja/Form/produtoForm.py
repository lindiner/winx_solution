from django.forms import ModelForm
from winx_sistema_loja.models import produto
from django.contrib.auth.forms import UserCreationForm

class ProdutoForm(ModelForm):
    class Meta:
        model = produto

        fields = ['name','precoProduto','codigoProduto','quantidadeEstoque']
