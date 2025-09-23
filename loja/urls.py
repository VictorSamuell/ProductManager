from django.urls import path
from . import views

urlpatterns = [

    path("", views.pagina_inicial, name="pagina_inicial"),
    path("produto/<slug:produto_slug>/", views.ver_produto_por_slug, name="ver_produto_por_slug"),
    path("base/", views.base, name="base"),
    path("produtos/", views.lista_produtos_view, name="lista_produtos"), 
    path("produtos/<int:produto_id>/", views.detalhe_produto_view, name="detalhe_produto"),

]