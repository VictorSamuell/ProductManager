# loja/models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Tabela 1: Cliente
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

# Tabela 2: Categoria
class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

# Tabela 3: Produto
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='produtos')
    estoque = models.PositiveIntegerField(default=0)
    #------ Novo Campo
    usuario = models.ForeignKey(
        User,
        on_delete=models.SET_NULL, #se o utilizador for apagado, o produto fica sem usuário
        null=True,
        blank=True
    )

    def valor_total_em_estoque(self):
        return self.preco * self.estoque
    valor_total_em_estoque.short_description = 'Valor total em estoque'

    def __str__(self):
        return self.nome
    

    imagem = models.ImageField(
        upload_to='produtos_imgs/',
        null = True,
        blank = True,
        help_text = "Imagem de destaque do produto"
    )

    def __str__(self):
        return self

# Tabela 4: Pedido
class Pedido(models.Model):
    STATUS_CHOICES = (
        ('P', 'Pendente'),
        ('A', 'Aprovado'),
        ('C', 'Cancelado'),
    )
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    data_pedido = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')

    def __str__(self):
        return f"Pedido {self.id} de {self.cliente.nome}"

# Tabela 5: ItemPedido (Tabela de Junção/Pivô)
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='ipedens')
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    

    def save(self,*args,**kwargs):
        if not self.preco_unitario and self.produto and self.produto.preco:
            self.preco_unitario = self.produto.preco
        super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome} no Pedido {self.pedido.id}"

class Autor(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.nome
    
