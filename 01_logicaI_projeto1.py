import json
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
0. Sair
'''
    opcoes = ['0', '1', '2', '3', '4', '5', '6']
    
    print('''
Escolha uma opção:''')
    opcao_usuario = input(texto_menu)

    while opcao_usuario not in opcoes:
        print('''
Opção Inválida!
Escolha uma opção corretamente:''')
        opcao_usuario = input(texto_menu)
    else:
        if opcao_usuario == '1':
            lista_categorias = sorted(listar_categorias(dados))
            print('\nLista de categorias:')
            for categoria in lista_categorias:
                print(categoria)
            menu(dados)
        elif opcao_usuario in ['2', '3', '4']:
            categoria = input('Informe a categoria que deseja consultar:\n')
            lista_categorias = sorted(listar_categorias(dados))
            while categoria not in lista_categorias:
                print('Categoria inválida.\nInforme corretamente a categoria:')
                categoria = input()
            else:
                if opcao_usuario == '2':
                    lista_produtos = listar_por_categoria(dados, categoria)
                    print(f'\nLista de produtos da categoria {categoria}:')
                    for produto in lista_produtos:
                        for chave, valor in produto.items():
                            if chave != 'categoria':
                                print(f'{chave}: {valor}') #ver se fica mais legal com end
                        print()
                    menu(dados)
                elif opcao_usuario == '3':
                    mais_caro_cat = produto_mais_caro(dados, categoria)
                    print(f'\nProduto mais caro da categoria {categoria}:')
                    for chave, valor in mais_caro_cat.items():
                        if chave != 'categoria':
                            print(f'{chave}: {valor}')
                    print()
                    menu(dados)
                elif opcao_usuario == '4':
                    mais_barato_cat = produto_mais_barato(dados, categoria)
                    print(f'\nProduto mais barato da categoria {categoria}:')
                    for chave, valor in mais_barato_cat.items():
                        if chave != 'categoria':
                            print(f'{chave}: {valor}')
                    print()
                    menu(dados)
        elif opcao_usuario == '5':
            lista_top_10_caros = top_10_caros(dados)
            print('\nTop 10 produtos mais caros:')
            for produto in lista_top_10_caros:
                for chave, valor in produto.items():
                    print(f'{chave}: {valor}')
                print()
            menu(dados)

        elif opcao_usuario == '6':
            lista_top_10_baratos = top_10_baratos(dados)
            print('\nTop 10 produtos mais baratos:')
            for produto in lista_top_10_baratos:
                for chave, valor in produto.items():
                    print(f'{chave}: {valor}')
                print()
            menu(dados)

        elif opcao_usuario == '0':
                print('\n\nAté breve!\n')

# Programa Principal - não modificar!
dados = obter_dados()
menu(dados)

# print(listar_categorias(dados))
# print(listar_por_categoria(dados, 'artes'))
# print(produto_mais_caro(dados, 'pcs'))
# print(produto_mais_barato(dados, 'pcs'))
# print(top_10_caros(dados))
# print(top_10_baratos(dados))

