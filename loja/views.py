from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import Produto

# Create your views here.

def pagina_inicial(request):
    # request is not used, but required by Django view signature
    return render(request, 'base.html')


def ver_produto_por_slug(request, produto_slug):
    # Use produto_slug in the response
    return HttpResponse(f"<h1> Produto </h1> <p> {produto_slug} </p>")

def base(request):
    return render(request, 'base.html')


def lista_produtos_view(request):
    produtos_disponiveis = Produto.objects.filter(estoque__gt=0).order_by("preco")
    return render(request, 'loja/lista_produto.html',{'PRODUTOS_DISPONIVEIS_LISTA': produtos_disponiveis})

def detalhe_produto_view(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'loja/detalhe_produto.html', {'produto': produto })

def produtos_caros_view(request):
    muitos_produtos_caros = Produto.objects.filter(estoque__gt=5 , preco__gt=500)
    return render(request, 'loja/produtos_caros.html',{'PRODUTOS_CAROS': muitos_produtos_caros})

def detalhe_produto_caro_view(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'loja/detalhe_produto_caro.html', {'produto': produto })

def sobre_view(request):
    return render(request, 'loja/sobre.html')

def contato_view(request):
    return render(request, 'loja/contato.html')


def produto_list_fbv(request):
    produtos_em_estoque = Produto.objects.filter(estoque__gt=0).order_by('nome')
    contexto = {
        'produtos': produtos_em_estoque,
        'titulo_da_pagina': 'Nossos Produtos Disponiveis'
    }

    return render(request, 'loja/produto_list.html', contexto)