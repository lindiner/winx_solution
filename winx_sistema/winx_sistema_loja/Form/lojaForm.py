from django.forms import ModelForm
from winx_sistema_loja.models import loja
from django.contrib.auth.forms import UserCreationForm

class LojaForm(ModelForm):
    class Meta:
        model = loja
<<<<<<< HEAD
        fields = ['nameLoja','endereco','emailLoja','telefoneLoja'] 
=======
        fields = ['nameLoja','emailLoja','telefoneLoja', 'cep','endereco', 'bairro','cidade'] 

>>>>>>> e6e713c597abb77099a2332d002362a19f9bbe26
