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
    contexto = {'produtos': produtos_disponiveis}
    return render(request, 'loja/lista_produto.html', contexto)

def detalhe_produto_view(request, produto_id):
        produto = get_object_or_404(Produto, id=produto_id)
        contexto = { 'produto': produto }
        return render(request, 'loja/detalhe_produto.html', contexto)