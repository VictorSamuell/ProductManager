from django import forms
from .models import Produto , Autor

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'categoria', 'estoque']

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'email']