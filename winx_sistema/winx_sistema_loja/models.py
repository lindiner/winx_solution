from django.db import models


class usuario(models.Model):
    idPessoa = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=128)
    email = models.EmailField( max_length=254)
    idade = models.DateField()
    cpf = models.CharField(max_length=14,null=False,blank=False)
    cep = models.CharField(max_length=8,null=False,blank=False)
    endereco = models.CharField(max_length=50)
    bairro = models.CharField( max_length=50)
    cidade = models.CharField( max_length=50)
    estado = models.CharField(max_length=40)

    

class vendedor(models.Model):
    codVendedor = models.IntegerField()
    usuario = models.ForeignKey(usuario,on_delete=models.CASCADE)
    


class loginAcessoS(models.Model):
    login = models.CharField(max_length=50, null=True)
    senha = models.CharField(max_length=50)
    pessoa = models.ForeignKey(usuario,on_delete=models.CASCADE)
   


class loja(models.Model):
    idLoja = models.UUIDField(primary_key=True)
    nameLoja = models.CharField(max_length=128)
    emailLoja = models.EmailField( max_length=254)
    telefoneLoja = models.IntegerField()
    cep = models.CharField(max_length=8,null=False,blank=False)
    endereco = models.CharField(max_length=50)
    bairro = models.CharField( max_length=50)
    cidade = models.CharField( max_length=50)

class categoria(models.Model):
    nomeCategoria = models.CharField(max_length=50)
    dt_criacao = models.DateTimeField(auto_now_add=False)

class produto(models.Model):
    idProduto = models.UUIDField(primary_key=True, default='')
    name = models.CharField(max_length=58,default='' )
    precoProduto = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    codigoProduto = models.IntegerField(default='')
    quantidadeEstoque = models.IntegerField(null=True)
    corProduto = models.CharField(max_length=50, null=True)
    tamanho = models.IntegerField(null=True)

    STATUS = (
        ('active', 'Ativo'),
        ('draft', 'Inativo')
        )

    status = models.CharField(max_length=15, choices=STATUS)
    vendedorCod = models.ForeignKey(vendedor,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.idProduto} ({self.vendedor.codVendedor})'

class avaliacao(models.Model):
    nota = models.IntegerField()
    comentario = models.TextField(max_length=240)
    categoriaAvaliacao = models.ForeignKey(categoria,on_delete=models.CASCADE)
    produtoAvaliado = models.ForeignKey(produto,on_delete=models.CASCADE)




class transacao(models.Model):
    data = models.DateField()
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField( max_digits=5, decimal_places=2)
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    produtoAvaliado = models.ForeignKey(produto,on_delete=models.CASCADE)
    usuarioTransacao = models.ForeignKey(usuario, on_delete=models.CASCADE)