from django.forms import ModelForm
from winx_sistema_loja.models import usuario
from winx_sistema_loja.models import loginAcessoS

class usuarioForm(ModelForm):
    class Meta:
        model = usuario
        fields = ['name', 'email','idade', 'cpf', 'cep', 'endereco', 'bairro', 'cidade', 'estado'] 


class usuarioLoginForm(ModelForm):
    class Meta:
        model = loginAcessoS
        fields = ['login', 'senha']

