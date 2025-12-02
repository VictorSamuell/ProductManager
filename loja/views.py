from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import Produto , Cliente
from django.views.generic import DetailView, ListView , UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .forms import AutorForm
from django.contrib.auth.decorators import login_required
from .serializer import ProdutoSerializer

from rest_framework import generics , status , viewsets
from rest_framework.response import Response
from rest_framework.views import APIView 

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

class ProdutoListView(ListView):
    model = Produto
    template_name = 'loja/produto_list.html'
    context_object_name = 'produtos'

    def get_queryset(self):
        return Produto.objects.filter(estoque__gt=0).order_by('nome')

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'loja/detail_product.html'
    context_object_name = 'produto'

def clienteList(request):
    clientes = Cliente.objects.all()
    contexto = {
        'clientes': clientes,
        'titulo_da_pagina': 'Nossos Clientes Disponiveis'
    }

    return render(request, 'loja/clienteList.html', contexto)

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'loja/detailCliente.html'
    context_object_name = 'cliente'

class RegistroView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registro.html'

class ProdutoCreateView(LoginRequiredMixin, CreateView):
    #atributos model, form class e outros

    def form_valid(self, form):
        # Antes de salvar define o usuario como cliente logado
        form.instance.usuario = self.request.user
        # Agora chama o método 'form_valid' original
        return super().form_valid(form)


class ProdutoUpdateView (LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    def test_func(self):
        #pega o produto que está ser editado
        produto = self.get_object()
        # Permite que só o utilizador da sessão for o autor do produto
        return self.request.user == produto.usuario
    

class ProdutoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    def test_func(self):
        produto = self.get_object()
        return self.request.user == produto.usuario
    
# class AutorCadastro()

@login_required
def cadastrar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o autor no banco de dados
            return redirect('autor_listar')  # Redireciona para uma página de listagem de autores (ou outra página)
    else:
        form = AutorForm()

    return render(request, 'cadastrar_autor.html', {'form': form})

class ProdutoListAPIView(APIView):

    def get(self, request, format=None):
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)
    pass

    def post(self, request, format=None):
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#class ProdutoListAPI(generics.ListCreateAPIView):


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all().order_by('nome')
    serializer_class = ProdutoSerializer

    def perform_create(self, serializer):
        def perform_create(self, serializer):
            serializer.save(autor=self.request.user)