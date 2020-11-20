from django.forms import ModelForm
from.models import usuario
from.model import loginAcessoS

class usuarioForm(ModelForm):
    class Meta:
        model = usuario
        fields = ['idPessoa', 'name', 'email','idade', 'cpf', 'cep', 'endereco', 'bairro', 'cidade', 'estado'] 


class usuarioLoginForm(ModelForm):
    class Meta:
        model = loginAcessoS
        fields = ['login', 'senha']




    
