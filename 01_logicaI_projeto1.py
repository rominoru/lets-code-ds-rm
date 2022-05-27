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
    return list({elemento['categoria'] for elemento in dados})

def listar_por_categoria(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar uma lista contendo todos os produtos pertencentes à categoria dada.
    '''
    return [elemento for elemento in dados if elemento['categoria'] == categoria]

def produto_mais_caro(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    return (sorted(listar_por_categoria(dados, categoria), key = lambda x: [float(x['preco'])], reverse = True))[0]
    
def produto_mais_barato(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    return (sorted(listar_por_categoria(dados, categoria), key = lambda x: [float(x['preco'])]))[0]

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
    mensagem_invalido = '\n----------------------------------------\nOpção Inválida!\n'
    opcoes = ['0', '1', '2', '3', '4', '5', '6']
    while opcao not in opcoes:
        opcao = input(f'{mensagem_invalido}Escolha corretamente uma opção:\n{texto_menu}\nOpção: ')
    return opcao

def validar_categoria(categoria, dados):
    mensagem_invalido = '----------------------------------------\nCategoria inválida.\nInforme corretamente a categoria:'
    while categoria.lower() not in sorted(listar_categorias(dados)):
        categoria = input(mensagem_invalido)        
    return categoria.lower()

def resultado(dados, opcao, categoria) -> str:
    '''Gera a saída em formato string a ser impressa em função da opção e categoria definidas no menu.
    Nas funções 2, 3 e 4, são informados id e preco, contextualmente fica reduntante informar a categoria do produto.
    Nas funções 5 e 6, são informados id, preco e categoria.'''
    titulos = {
        '1': '\nLista de categorias:\n',
        '2': '\nLista de produtos da categoria ',
        '3': '\nProduto mais caro da categoria ',
        '4': '\nProduto mais barato da categoria ',
        '5': '\nTop 10 produtos mais caros:',
        '6': '\nTop 10 produtos mais baratos:'
    }
    resultado = titulos[opcao]
    
    if opcao == '1':
        contador = 1
        for item in sorted(listar_categorias(dados)):
            resultado += str(contador) + '. ' + item.upper() + '\n'
            contador += 1
        return resultado
    
    elif opcao == '2':
        resultado += categoria.upper() + ':'
        contador = 1
        for produto in listar_por_categoria(dados, categoria):
            resultado += '\n' + str(contador) + '.\n'
            for chave, valor in produto.items():
                if chave != 'categoria':
                    resultado += chave + ': ' + valor.upper() + '\n'
            contador += 1
        return resultado

    elif opcao == '3':
        resultado += categoria.upper() + ':\n'
        for chave, valor in produto_mais_caro(dados, categoria).items():
            if chave != 'categoria':
                resultado += chave + ': ' + valor.upper() + '\n'                
        return resultado

    elif opcao == '4':
        resultado += categoria.upper() + ':\n'
        for chave, valor in produto_mais_barato(dados, categoria).items():
            if chave != 'categoria':
                resultado += chave + ': ' + valor.upper() + '\n'                
        return resultado

    elif opcao == '5':
        contador = 1
        for produto in top_10_caros(dados):
            resultado += '\n' + str(contador) + '.\n'
            for chave, valor in produto.items():
                resultado += chave + ': ' + valor.upper() + '\n'
            contador += 1
        return resultado

    elif opcao == '6':
        contador = 1
        for produto in top_10_baratos(dados):
            resultado += '\n' + str(contador) + '.\n'
            for chave, valor in produto.items():
                resultado += chave + ': ' + valor.upper() + '\n'
            contador += 1
        return resultado

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
    mensagem_escolha = '\n----------------------------------------\nEscolha uma opção:\n'
    texto_menu = '''----------------------------------------
1. Listar categorias
2. Listar produtos de uma categoria
3. Produto mais caro por categoria
4. Produto mais barato por categoria
5. Top 10 produtos mais caros
6. Top 10 produtos mais baratos
0. Sair
----------------------------------------'''    

    opcao = input(f'{mensagem_escolha}{texto_menu}\nOpção: ')
    opcao = validar_opcao(opcao, texto_menu)
    categoria = ''

    while opcao != '0':
        if opcao in ['2', '3', '4']:
            categoria = input('Informe a categoria que deseja consultar:\n')
            categoria = validar_categoria(categoria, dados)
        print(resultado(dados, opcao, categoria))

        opcao = input(f'{mensagem_escolha}{texto_menu}\nOpção: ')
        opcao = validar_opcao(opcao, texto_menu)
    else:
        print('\n\nAté breve!\n')

# Programa Principal - não modificar!
dados = obter_dados()
menu(dados)

