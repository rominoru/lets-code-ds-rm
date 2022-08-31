## Enunciado
Para implementar o programa abaixo, tente empregar técnicas estudadas no módulo atual quando possível: tratamento de strings, manipulação de arquivos utilizando as bibliotecas auxiliares estudadas (`csv` e `json`), tratamento de exceção, diferentes formatos de parâmetro de função, compreensão de listas e/ou geradores, funções de alta ordem e lambda. Apesar de ser possível resolver boa parte dos problemas utilizando loops e técnicas do módulo anterior, você deixará de treinar os novos conceitos e perderá a oportunidade de receber feedback adequado sobre o seu aprendizado deste módulo.
Uma grande dificuldade de muitos músicos de garagem é encontrar outros músicos que toquem instrumentos diferentes, possuam gostos semelhantes e disponibilidade para formar conjuntos.
Vamos fazer um sistema para auxiliar na formação de bandas online! Em seu menu principal, o programa deverá oferecer as seguintes funcionalidades:
- Cadastrar músicos
- Buscar músicos
- Modificar músicos
- Montar bandas
- Sair

**No cadastro** devem ser digitadas as seguintes informações:

- Nome (string contendo apenas letras e espaço)
- E-mail (string contendo apenas letras, underscore (`_`), ponto (`.`), dígitos numéricos e, obrigatoriamente, exatamente 1 arroba (`@`))
- Gêneros musicais (mínimo 1, usuário pode digitar quantos forem necessários)
- Instrumentos (mínimo 1, usuário pode digitar quantos forem necessários)


As entradas devem ser validadas seguindo as regras. O e-mail deve ser único: se ele já existe, o cadastro não deve ser concluído.

DICA: padronize suas strings na hora de salvar em sua base para evitar que buscas sejam prejudicadas por divergências de maiúsculas e minúsculas.

**Na busca** o usuário deve passar pelo menos 1 das opções: nome, e-mail, gênero (digitar apenas 1) ou instrumento (digitar apenas 1). O usuário deve selecionar se os resultados devem bater com todas as informações digitadas ou pelo menos uma (ex: se o usuário digitar nome e instrumento, a busca pode ser por resultados contendo o nome E o instrumento vs o nome OU o instrumento).

**Na modificação de um usuário**, será feita uma busca especificamente por e-mail. É permitido adicionar ou remover gêneros e instrumentos. Não é permitido mudar nome ou e-mail.

**Na opção de montar bandas**, o usuário deverá informar o número desejado de músicos, o instrumento de cada um dos músicos (1 por músico) e 1 gênero. O programa deverá exibir na tela todas as combinações possíveis de músicos (e-mail + instrumento).

Ex: suponha que para o gênero 'heavy metal' a gente tenha os músicos ana@letscode.com.br (bateria), bruno@letscode.com.br (guitarra), carol@letscode.com.br (guitarra), danilo@letscode.com.br (baixo) e erasmo@letscode.com.br (baixo) e a busca seja:
- Gênero: heavy metal
- Quantidade: 3
- Instrumento 1: guitarra
- Instrumento 2: bateria
- Instrumento 3: baixo

A saída mostraria as seguintes combinações:
```
(bruno@letscode.com.br, guitarra) + (ana@letscode.com.br, bateria) + (danilo@letscode.com.br, baixo)
(bruno@letscode.com.br, guitarra) + (ana@letscode.com.br, bateria) + (erasmo@letscode.com.br, baixo)
(carol@letscode.com.br, guitarra) + (ana@letscode.com.br, bateria) + (danilo@letscode.com.br, baixo)
(carol@letscode.com.br, guitarra) + (ana@letscode.com.br, bateria) + (erasmo@letscode.com.br, baixo)
```

A formatação para exibir esse resultado fica a seu critério.

O seu programa deverá salvar todos os dados em formato de sua preferência para consulta posterior: JSON ou CSV.

Caso opte por CSV, ele terá as colunas nome, e-mail, instrumentos (escreva os dados em formato de lista) e gêneros (escreva os dados em formato de lista). Ex:
```
ana;ana@letscode.com.br;['bateria', 'voz'];['hard rock', 'heavy metal']
bruno;bruno@letscode.com.br;['guitarra'];['heavy metal', 'jazz']
```
Para o JSON, teremos uma lista de dicionários. As chaves dos dicionários correspondem às colunas do CSV. Alternativamente, você pode fazer um dicionário de dicionários, adotando o e-mail como chave, e o valor seria um dicionário contendo as outras 3 chaves.

Lembre-se de garantir que seu programa sempre salva o arquivo quando for encerrado.

