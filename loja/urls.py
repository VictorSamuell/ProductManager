from django.urls import path, include
from . import views
from .views import (
    ProdutoListView,
    ProdutoDetailView,
    ProdutoDeleteView,
    ProdutoCreateView,
    ProdutoUpdateView,
    ProdutoListAPIView,
    RegistroView,
    ClienteDetailView,
)



urlpatterns = [

    #

    path("", views.pagina_inicial, name="pagina_inicial"),

    #

    path("produto/<slug:produto_slug>/", views.ver_produto_por_slug, name="ver_produto_por_slug"),

    # base.html

    path("base/", views.base, name="base"),

    # 

    path("produtos/", views.lista_produtos_view, name="lista_produtos"), 
    
    # detalhe_produto.html

    path("det_produtos/<int:produto_id>/", views.detalhe_produto_view, name="detalhe_produto"),
    
    # detalhe_produto_caro.html

    path("det_produtos_caros/<int:produto_id>/", views.detalhe_produto_caro_view, name="detalhe_produto_caro"),
    
    #

    path("expensive/", views.produtos_caros_view , name="produtos_caros"),
    
    # sobre.html
    
    path("sobre/", views.sobre_view , name="sobre"),
    
    #  contato.html
    
    path("contato/", views.contato_view, name="contato"),
    
    # produto_list.html - Function Based View (FBV)
    
    path("produto_list_fbv/", views.produto_list_fbv, name="produto_list_fbv"),

    #

    path("produto_list/<int:pk>/", ProdutoDetailView.as_view(), name="produto_detail"),

    #

    path("cliente_list/", views.clienteList, name="cliente_list"),

    #

    path("cliente_list/<int:pk>/", ClienteDetailView.as_view(), name="cliente_detail"),

    # `admin` and project-level includes are handled in `config/urls.py`

    # 
    path('contas/registro/', RegistroView.as_view(), name = 'registro'),

    path('contas/', include('django.contrib.auth.urls')),


    path('cadastrar/', views.cadastrar_autor, name='cadastrar_autor'),
    # Adicione outras URLs, como a de listagem de autores, se necessário

    # removed duplicate and malformed admin/include entries

    path('api/produtos/', ProdutoListAPIView.as_view(), name='api_produto_list_view'),

    path('', ProdutoListView.as_view(), name='produto_list'),


]