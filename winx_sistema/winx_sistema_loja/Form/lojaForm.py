from django.forms import ModelForm
from winx_sistema_loja.models import loja
from django.contrib.auth.forms import UserCreationForm

class LojaForm(ModelForm):
    class Meta:
        model = loja
        fields = ['nameLoja','endereco','emailLoja','telefoneLoja'] 
