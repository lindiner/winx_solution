from django.forms import ModelForm
from.models import usuario

class usuarioForm(ModelForm):
    class Meta:
        model = usuario
        fields = ['idPessoa', 'name', 'email','idade', 'cpf', 'cep', 'endereco', 'bairro', 'cidade', 'estado'] 