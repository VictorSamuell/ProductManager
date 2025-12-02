from django import forms
from .models import Autor , Produto

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'email']


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'categoria', 'estoque', 'imagem']