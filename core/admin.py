from django.contrib import admin

# Register your models here.

from .models import Produto, Cliente

##adicionard mais informações na interface do admin

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor', 'estoque')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)