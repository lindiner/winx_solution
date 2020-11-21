from django.forms import ModelForm
from winx_sistema_loja.models import usuario
from winx_sistema_loja.models import loginAcessoS
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(ModelForm):
    class Meta:
        model = usuario
        fields = ['name', 'email','idade', 'endereco', 'cpf'] 


class UsuarioLoginForm(ModelForm):
    class Meta:
        model = loginAcessoS
        fields = ['login', 'senha']

