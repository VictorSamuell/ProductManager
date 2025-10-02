from django.contrib import admin
from .models import Produto, Categoria, Cliente, ItemPedido, Pedido

@admin.action(description="Zerar estoque dos produtos selecionados")
def zerarEstoque(modeladmin, request, queryset):
    queryset.update(estoque=0)
    
@admin.action(description="Marcar Estoque como Pendente")
def marcar_como_pendente(modeladmin, request, queryset):
    queryset.update(status="P")


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display=('nome','descricao','preco', 'categoria', 'estoque')
    
    list_filter = ('categoria','estoque')
    
    search_fields = ('nome','preco')
    
    
    actions = [zerarEstoque]
    
   


    
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_cadastro')
    
    search_fields = ('nome','email')
    
    readonly_fields = ('data_cadastro',)
    



class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    
    fields = ('produto','quantidade','preco_unitario')
    
    readonly_fields  = ('preco_unitario',)
    
    extra = 1
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        
        if db_field.name == "produto":
            pass
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
       
       
@admin.register(Pedido)       
class PedidoAdmin(admin.ModelAdmin):
    
    @admin.display(description="Valor Total")
    def valor_total(self, obj):
        return sum(i.quantidade * i.preco_unitario for i in obj.ipedens.all())
    
    @admin.display(description="Self")
    def selfzao(self, obj):
        return f"{self} & {obj}"



    list_display = ('id','cliente','data_pedido','status', 'valor_total', 'selfzao')
     
    list_filter = ('status','data_pedido')
     
    data_hierarchy = 'data_pedido'
      
    inlines = [ItemPedidoInline]
     
    raw_id_fields = ('cliente',)

    actions = [marcar_como_pendente]


