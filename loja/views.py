from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import Produto , Cliente , Autor
from django.views.generic import DetailView, ListView , CreateView , UpdateView , DeleteView
from .forms import ProdutoForm , AutorForm
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status , generics , viewsets





from .serializers import ProdutoSerializer , CategoriaSerializer

# Create your views here.

def pagina_inicial(request):
    # request is not used, but required by Django view signature
    return render(request, 'base.html')

def base(request):
    return render(request, 'base.html')

def lista_produtos_view(request):
    produtos_disponiveis = Produto.objects.filter(estoque__gt=0).order_by("preco")
    return render(request, 'loja/lista_produto.html',{'PRODUTOS_DISPONIVEIS_LISTA': produtos_disponiveis})

def detalhe_produto_view(request, pk):
    # aceitar 'pk' para compatibilidade com reverse() que usa kwargs 'pk'
    produto = get_object_or_404(Produto, id=pk)
    return render(request, 'loja/detalhe_produto.html', {'produto': produto })

def produtos_caros_view(request):
    muitos_produtos_caros = Produto.objects.filter(estoque__gt=5 , preco__gt=500)
    return render(request, 'loja/produtos_caros.html',{'PRODUTOS_CAROS': muitos_produtos_caros})

def detalhe_produto_caro_view(request, pk):
    # aceitar 'pk' para compatibilidade com reverse() que usa kwargs 'pk'
    produto = get_object_or_404(Produto, id=pk)
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

def ProdutoListView(ListView):
    model = Produto
    template_name = 'loja/produto_list.html'
    context_object_name = 'produtos'

    def get_queryset(self):
        return Produto.objects.filter(estoque__gt=0).order_by('nome')


def clienteList(request):
    clientes = Cliente.objects.all()
    contexto = {
        'clientes': clientes,
        'titulo_da_pagina': 'Nossos Clientes Disponiveis'
    }

    return render(request, 'loja/clienteList.html', contexto)


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'loja/cliente_detail.html'
    context_object_name = 'cliente'

class ProdutoListView(ListView):
    model = Produto
    template_name = 'loja/produto_list.html'
    context_object_name = 'produtos'
    # Query para mostrar apenas produtos com estoque, ordenados por nome
    queryset = Produto.objects.filter(estoque__gt=0).order_by('nome')

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'loja/detalhe_produto.html'
    context_object_name = 'produto'


class ProdutoCreateView(LoginRequiredMixin, CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'loja/produto_form.html'
    success_url = reverse_lazy('produto_list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class ProdutoUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'loja/produto_form.html'
    success_url = reverse_lazy('produto_list')

    def test_func(self):
        produto = self.get_object()
        # DEBUG: permitir edição para qualquer usuário autenticado (temporário)
        # Isso ajuda a diagnosticar 403s; em produção você pode restringir novamente
        return self.request.user.is_authenticated or (produto.usuario is None) or (self.request.user == produto.usuario) or self.request.user.is_superuser

class ProdutoDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Produto
    template_name = 'loja/produto_confirm_delete.html'
    success_url = reverse_lazy('produto_list')

    def test_func(self):
        produto = self.get_object()
        # DEBUG: permitir exclusão para qualquer usuário autenticado (temporário)
        return self.request.user.is_authenticated or (produto.usuario is None) or (self.request.user == produto.usuario) or self.request.user.is_superuser

class RegistroView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registro.html'



# AUTOR 

class AutorListView(ListView):
    model = Autor
    template_name = 'loja/autor_list.html'
    context_object_name = 'autores'
    # Query para mostrar apenas produtos com estoque, ordenados por nome
    queryset = Autor.objects.all().order_by('nome')

class AutorDetailView(DetailView):
    model = Autor
    template_name = 'loja/detalhe_autor.html'
    context_object_name = 'autor'


class AutorCreateView(LoginRequiredMixin, CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'loja/autor_form.html'
    success_url = reverse_lazy('autor_list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class AutorUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'loja/autor_form.html'
    success_url = reverse_lazy('autor_list')

    def test_func(self):
        autor = self.get_object()
        # DEBUG: permitir edição para qualquer usuário autenticado (temporário)
        return self.request.user.is_authenticated or (autor.usuario is None) or (self.request.user == autor.usuario) or self.request.user.is_superuser

class AutorDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Autor
    template_name = 'loja/autor_confirm_delete.html'
    success_url = reverse_lazy('autor_list')

    def test_func(self):
        autor = self.get_object()
        # DEBUG: permitir exclusão para qualquer usuário autenticado (temporário)
        return self.request.user.is_authenticated or (autor.usuario is None) or (self.request.user == autor.usuario) or self.request.user.is_superuser


class ProdutoListAPIView(APIView):
    def get(self, request, format=None):

        produtos = Produto.objects.all()
        
        serializer = ProdutoSerializer(produtos, many=True)

        return Response(serializer.data)
    
    def post(self, request, format=None):

        serializer = ProdutoSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class ProdutoListAPI(generics.ListCreatedAPIView):
#     queryset = Produto.objects.all()
#     serializer_class = ProdutoSerializer

# class ProdutoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Produto.objects.all()
#     serializer_class = ProdutoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)