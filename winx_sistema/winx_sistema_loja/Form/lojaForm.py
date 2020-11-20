from django.forms import ModelForm
from winx_sistema_loja.models import loja

class lojaForm(ModelForm):
    class Meta:
        model = loja
        fields = ['nameLoja','emailLoja','telefoneLoja', 'cep','endereco', 'bairro','cidade'] 

 
