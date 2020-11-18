from django.contrib import admin
from .models import usuario
from .models import loginAcessoS
from .models import produto
from .models import loja
from .models import vendedor
from .models import categoria
from .models import avaliacao
from .models import transacao


admin.site.register(vendedor)
admin.site.register(loginAcessoS)
admin.site.register(produto)
admin.site.register(loja)
admin.site.register(categoria)
admin.site.register(usuario)
admin.site.register(transacao)
admin.site.register(avaliacao)

# Register your models here.
