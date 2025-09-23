import os
import django
import random
from decimal import Decimal
from faker import Faker

# --- Configuração do Ambiente Django ---
# Define o arquivo de settings do seu projeto
# Altere 'meuprojeto.settings' para o nome da pasta do seu projeto.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
# --- Fim da Configuração ---

# Agora podemos importar os models, pois o ambiente Django está configurado
from loja.models import Cliente, Categoria, Produto, Pedido, ItemPedido

def popular_banco():
    """
    Função principal que limpa e popula as tabelas do banco de dados.
    """
    print("Iniciando o povoamento do banco de dados...")

    fake = Faker('pt_BR')

    # Limpando dados existentes para evitar duplicatas
    print("Limpando tabelas antigas...")
    ItemPedido.objects.all().delete()
    Pedido.objects.all().delete()
    Produto.objects.all().delete()
    Categoria.objects.all().delete()
    Cliente.objects.all().delete()

    # --- Gerar 50 Clientes ---
    clientes = []
    for _ in range(50):
        clientes.append(Cliente(nome=fake.name(), email=fake.unique.email()))
    Cliente.objects.bulk_create(clientes)
    print("✅ 50 Clientes criados com sucesso!")

    # --- Gerar 5 Categorias ---
    nomes_categorias = ['Eletrônicos', 'Livros', 'Roupas', 'Casa e Cozinha', 'Esportes']
    categorias = []
    for nome in nomes_categorias:
        categorias.append(Categoria(nome=nome))
    Categoria.objects.bulk_create(categorias)
    print(f"✅ {len(nomes_categorias)} Categorias criadas com sucesso!")

    # --- Gerar 50 Produtos ---
    lista_categorias = list(Categoria.objects.all())
    produtos = []
    for _ in range(50):
        produtos.append(Produto(
            nome=fake.bs().capitalize(),
            descricao=fake.text(max_nb_chars=200),
            preco=Decimal(random.uniform(10.50, 999.99)).quantize(Decimal('0.01')),
            categoria=random.choice(lista_categorias),
            estoque=random.randint(10, 100)
        ))
    Produto.objects.bulk_create(produtos)
    print("✅ 50 Produtos criados com sucesso!")

    # --- Gerar 50 Pedidos ---
    lista_clientes = list(Cliente.objects.all())
    pedidos = []
    for _ in range(50):
        pedidos.append(Pedido(
            cliente=random.choice(lista_clientes),
            status=random.choice(['P', 'A', 'C'])
        ))
    Pedido.objects.bulk_create(pedidos)
    print("✅ 50 Pedidos criados com sucesso!")

    # --- Gerar 50 Itens de Pedido ---
    lista_pedidos = list(Pedido.objects.all())
    lista_produtos = list(Produto.objects.all())
    itens_pedido = []
    for i in range(50): # Garante pelo menos um item por pedido
        produto_escolhido = random.choice(lista_produtos)
        itens_pedido.append(ItemPedido(
            pedido=lista_pedidos[i],
            produto=produto_escolhido,
            quantidade=random.randint(1, 5),
            preco_unitario=produto_escolhido.preco
        ))
    ItemPedido.objects.bulk_create(itens_pedido)
    print("✅ 50 Itens de Pedido criados com sucesso!")

    print("\n🎉 Banco de dados populado com sucesso!")

# Garante que a função só será executada quando o script for chamado diretamente
if __name__ == '__main__':
    popular_banco()