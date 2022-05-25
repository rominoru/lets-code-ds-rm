import json
from operator import contains
import os.path
import sys

def obter_dados():
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um produto.
    NÃO MODIFIQUE essa função.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

def listar_categorias(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista contendo todas as categorias dos diferentes produtos.
    Cuidado para não retornar categorias repetidas.    
    '''
    lista_categorias = []
    for elemento in dados:
        if elemento['categoria'] not in lista_categorias: lista_categorias.append(elemento['categoria'])
    return lista_categorias

def listar_por_categoria(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar uma lista contendo todos os produtos pertencentes à categoria dada.
    '''
    lista_produtos = []
    for elemento in dados:
        if elemento['categoria'] == categoria: lista_produtos.append(elemento)
    return lista_produtos

def produto_mais_caro(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''

    lista_categoria = []
    for elemento in dados:
        if elemento['categoria'] == categoria: lista_categoria.append(elemento)
    return (sorted(lista_categoria, key = lambda x: [float(x['preco'])], reverse = True))[0]

    # list comprehension não foi passado em aula:
    # lista_categoria = [elemento for elemento in dados if elemento['categoria'] == categoria]
    # return (sorted(lista_categoria, key = lambda x: [float(x['preco'])], reverse = True))[0]

    # solução mais manual
    # preco_mais_alto = float('-inf')
    # produto_mais_caro = {}
    # for elemento in dados:
    #     if elemento['categoria'] == categoria and float(elemento['preco']) > float(preco_mais_alto):
    #         preco_mais_alto, produto_mais_caro = elemento['preco'], elemento
    # return produto_mais_caro

def produto_mais_barato(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    
    lista_categoria = []
    for elemento in dados:
        if elemento['categoria'] == categoria: lista_categoria.append(elemento)
    return (sorted(lista_categoria, key = lambda x: [float(x['preco'])]))[0]

    # list comprehension não foi passado em aula:
    # lista_categoria = [elemento for elemento in dados if elemento['categoria'] == categoria]
    # return (sorted(lista_categoria, key = lambda x: [float(x['preco'])]))[0]

    # solução mais manual
    # preco_mais_baixo = float('inf')
    # produto_mais_barato = {}
    # for elemento in dados:
    #     if elemento['categoria'] == categoria and float(elemento['preco']) < float(preco_mais_baixo):
    #         preco_mais_baixo, produto_mais_barato = elemento['preco'], elemento
    # return produto_mais_barato

def top_10_caros(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    return sorted(dados, key = lambda x: [float(x['preco'])], reverse = True)[:10]
    
def top_10_baratos(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais baratos.
    '''
    return sorted(dados, key = lambda x: [float(x['preco'])])[:10]

def validar_opcao(opcao, texto_menu):
    opcoes = ['0', '1', '2', '3', '4', '5', '6']
    while opcao not in opcoes:
        opcao = input(f'\nOpção Inválida!\nEscolha uma opção corretamente:\n{texto_menu}\nOpção: ')
    return opcao

def validar_categoria(categoria, dados):
    while categoria.lower() not in sorted(listar_categorias(dados)): #DÚVIDA, ativar função dentro da função
        categoria = input('Categoria inválida.\nInforme corretamente a categoria:')        
    return categoria.lower()

def print_lista_categorias(categorias: list) -> None:
    '''
    Imprime as categorias de uma lista de categorias.
    '''
    contador = 1
    for categoria in categorias:
        print(f'{contador}. {categoria.upper()}')
        contador += 1

def print_lista_produto(produtos: list) -> None:
    '''
    Imprime id, preco e categoria de uma lista de produtos.
    '''
    contador = 1
    for produto in produtos:
        print(f'{contador}.')
        for chave, valor in produto.items():
            print(f'{chave}: {valor.upper()}')
        print()
        contador += 1

def print_lista_sem_cat(produtos: list) -> None:
    '''
    Imprime id e preco de uma lista de produtos. Não imprime a categoria.
    Utilizar quando for redundante informar a categoria.
    '''
    contador = 1
    for produto in produtos:
        print(f'{contador}.')
        # print_produto_sem_cat(produto)
        for chave, valor in produto.items():
            if chave != 'categoria':
                print(f'{chave}: {valor}')
        print()
        contador += 1    

def print_produto_sem_cat(produto: dict) -> None:
    '''
    Imprime id e preco de determinado produto. Não imprime a categoria.
    Utilizar quando for redundante informar a categoria.
    '''
    for chave, valor in produto.items():
        if chave != 'categoria':
            print(f'{chave}: {valor}')
    print()

def menu(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá, em loop, realizar as seguintes ações:
    - Exibir as seguintes opções:
        1. Listar categorias
        2. Listar produtos de uma categoria
        3. Produto mais caro por categoria
        4. Produto mais barato por categoria
        5. Top 10 produtos mais caros
        6. Top 10 produtos mais baratos
        0. Sair
    - Ler a opção do usuário.
    - No caso de opção inválida, imprima uma mensagem de erro.
    - No caso das opções 2, 3 ou 4, pedir para o usuário digitar a categoria desejada.
    - Chamar a função adequada para tratar o pedido do usuário e salvar seu retorno.
    - Imprimir o retorno salvo. 
    O loop encerra quando a opção do usuário for 0.
    '''
    
    texto_menu = '''1. Listar categorias
2. Listar produtos de uma categoria
3. Produto mais caro por categoria
4. Produto mais barato por categoria
5. Top 10 produtos mais caros
6. Top 10 produtos mais baratos
0. Sair'''    

    opcao = input(f'\nEscolha uma opção:\n{texto_menu}\nOpção: ')
    opcao = validar_opcao(opcao, texto_menu)

    while opcao != '0':
        if opcao in ['2', '3', '4']:
            categoria = input('Informe a categoria que deseja consultar:\n')
            categoria = validar_categoria(categoria, dados)

        if opcao == '1':
            print('\nLista de categorias:')
            print_lista_categorias(sorted(listar_categorias(dados)))
        elif opcao == '2':
            print(f'\nLista de produtos da categoria {categoria.upper()}:')
            print_lista_sem_cat(listar_por_categoria(dados, categoria))
        elif opcao == '3':
            print(f'\nProduto mais caro da categoria {categoria.upper()}:')
            print_produto_sem_cat(produto_mais_caro(dados, categoria))
        elif opcao == '4':
            print(f'\nProduto mais barato da categoria {categoria.upper()}:')
            print_produto_sem_cat(produto_mais_barato(dados, categoria))
        elif opcao == '5':
            print('\nTop 10 produtos mais caros:')
            print_lista_produto(top_10_caros(dados))
        elif opcao == '6':
            print('\nTop 10 produtos mais baratos:')
            print_lista_produto(top_10_baratos(dados))
        opcao = input(f'\nEscolha uma opção:\n{texto_menu}\nOpção: ')
        opcao = validar_opcao(opcao, texto_menu)
    else:
        print('\n\nAté breve!\n')

# Programa Principal - não modificar!
dados = obter_dados()
menu(dados)

