from django.contrib import admin
from .models import Produto, Categoria
from django.contrib.admin import ModelAdmin

# Register your models here.


class ProdutoAdmin(ModelAdmin):
    list_display = ('nome','descricao','preco','categoria','estoque')
    list_filter = ('nome', 'preco')
    search_fields = ('nome', 'preco')

admin.site.register(Produto,ProdutoAdmin)
admin.site.register(Categoria)