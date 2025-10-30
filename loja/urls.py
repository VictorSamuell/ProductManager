from django.urls import path
from . import views
from .views import ProdutoCreateView , ProdutoDetailView , ProdutoListView ,ProdutoUpdateView , ProdutoDeleteView

urlpatterns = [

    #

    path("", views.base, name="base"),


    # lista de produtos (CBV) — mantém nome esperado 'produto_list'
    path("produtos/", ProdutoListView.as_view(), name="produto_list"),

    # detalhe_produto.html

    path("det_produtos/<int:pk>/", views.detalhe_produto_view, name="detalhe_produto"),
    
    # detalhe_produto_caro.html

    path("det_produtos_caros/<int:pk>/", views.detalhe_produto_caro_view, name="detalhe_produto_caro"),
    
    #

    path("expensive/", views.produtos_caros_view , name="produtos_caros"),
    
    # sobre.html
    
    path("sobre/", views.sobre_view , name="sobre"),
    
    #  contato.html
    
    path("contato/", views.contato_view, name="contato"),
    
    # produto_list.html - Function Based View (FBV)
    
    path("produto_list_fbv/", views.produto_list_fbv, name="produto_list_fbv"),

    path("cliente_list/", views.clienteList, name="cliente_list"),
    path('cliente/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente_detail'),

    # CRUD para Produto (CBV)
    path('produto/novo/', ProdutoCreateView.as_view(), name='produto_create'),
    path('produto/<int:pk>/', ProdutoDetailView.as_view(), name='produto_detail'),
    path('produto/<int:pk>/editar/', ProdutoUpdateView.as_view(), name='produto_update'),
    path('produto/<int:pk>/apagar/', ProdutoDeleteView.as_view(), name='produto_delete'),
    
    # registro é servido em 'contas/registro/' (definido em config.urls) — evitar duplicação de nomes

    
]
