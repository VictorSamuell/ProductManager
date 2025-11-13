from rest_framework import serializers
from .models import Produto , Categoria

class ProdutoSerializer(serializers.ModelSerializer):
    
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())
    categoria_nome = serializers.StringRelatedField(source='categoria', read_only=True)
    autor = serializers.StringRelatedField()

    class Meta:
        model = Produto
        fields = [
            'id',
            'nome',
            'descricao',
            'preco',
            'categoria',
            'categoria_nome',
            'estoque',
            'imagem',
            'autor',
        ]

        extra_kwargs = {
            'categoria': {'write_only': True},
            'autor': {'write_only': True},
        }


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = [
            'id',
            'nome'
        ]

   