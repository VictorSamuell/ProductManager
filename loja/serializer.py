from rest_framework import serializers
from .models import Produto, Categoria
from django.contrib.auth.models import User

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome']

class ProdutoSerializer(serializers.ModelSerializer):

    categoria = serializers.StringRelatedField(source='categoria', read_only=True)
    usuario = serializers.StringRelatedField(source='usuario', read_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='usuario', write_only=True)

    class Meta:
        model = Produto

        fields = [
            'id',
            'nome',
            'descricao',
            'preco',
            'estoque',
            'imagem',
            'categoria',
            'usuario',
            'categoria',
            'usuario_id', 

            'categoria_nome',
            'usuario'
        ]

        extra_kwargs = {
            'categoria': {'write_only': True},
        }

