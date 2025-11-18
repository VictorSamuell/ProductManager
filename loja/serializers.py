from rest_framework import serializers
from .models import Produto , Categoria
from django.contrib.auth.models import User

class ProdutoSerializer(serializers.ModelSerializer):
    
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())
    categoria_nome = serializers.StringRelatedField(source='categoria', read_only=True)
    # autor = serializers.StringRelatedField()
    usuario = serializers.PrimaryKeyRelatedField(source='User', read_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),source='User', write_only=True)


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
            'usuario',
            'usuario_id'
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

   