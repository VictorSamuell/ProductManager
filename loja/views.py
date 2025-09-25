from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import Produto

# Create your views here.

def pagina_inicial(request):
    # request is not used, but required by Django view signature
    return HttpResponse("<h1> WELCOME TO THE STORE! </h1> <p> É nois caralho </p>")


def ver_produto_por_slug(request, produto_slug):
    # Use produto_slug in the response
    return HttpResponse(f"<h1> Produto </h1> <p> {produto_slug} </p>")

def base(request):
    return render(request, 'base.html')


def lista_produtos_view(request):
    produtos_disponiveis = Produto.objects.filter(estoque__gt=0)
    return render(request, 'loja/lista_produto.html',{'PRODUTOS_DISPONIVEIS_LISTA': produtos_disponiveis})

def detalhe_produto_view(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'loja/detalhe_produto.html', {'produto': produto })

def sobre_view(request):
    return render(request, 'loja/sobre.html')

def contato_view(request):
    return render(request, 'loja/contato.html')