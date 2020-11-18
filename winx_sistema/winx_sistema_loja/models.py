from django.db import models

# Create your models here.
class vendedor(models.Model):
    idpessoa = models.AutoField(primary_key=True)
    codVendedor = models.models.IPAddressField(_(""))
    name = models.CharField(max_length=128)
    email = models.EmailField(_(""), max_length=254)
    idade = models.models.DateField(_(""), auto_now=False, auto_now_add=False)
    cpf = models.BinaryField(_(""))
    cnpj = models.BigAutoField(_(""))
    cep = models.models.BigAutoField(_(""))
    endereco = models.CharField(_(""), max_length=50)
    bairro = models.CharField(_(""), max_length=50)
    cidade = models.CharField(_(""), max_length=50)
    estado = models.CharField(_(""), max_length=50)


class login(models.Model):
    usuario = models.CharField(max_length=50)
    senha = models.models.TextField(_(""))
    vendedor = models.ManyToManyField(vendedor.idpessoa)


class Produto(models.Model):
    STATUS = (
        ('active', 'Ativo'),
        ('draft', 'Inativo')
        )

    status = models.CharField(max_length=15, choices=STATUS)