from django.forms import ModelForm
from.models import loja

class lojaForm(ModelForm):
    class Meta:
        model = loja
        fields = ['idLoja','nameLoja','emailLoja','telefoneLoja', 'cep','endereco', 'bairro','cidade'] 
 