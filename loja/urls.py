from django.urls import path
from . import views

urlpatterns = [

    path("", views.pagina_inicial, name="pagina_inicial"),
    path("produto/<slug:produto_slug>/", views.ver_produto_por_slug, name="ver_produto_por_slug"),
    path("base/", views.base, name="base"),
    path("produtos/", views.lista_produtos_view, name="lista_produtos"), 
    path("det_produtos/<int:produto_id>/", views.detalhe_produto_view, name="detalhe_produto"),
    path("det_produtos_caros/<int:produto_id>/", views.detalhe_produto_caro_view, name="detalhe_produto_caro"),
    path("expensive/", views.produtos_caros_view , name="produtos_caros"),
    path("sobre/", views.sobre_view , name="sobre"),
    path("contato/", views.contato_view, name="contato"),

]