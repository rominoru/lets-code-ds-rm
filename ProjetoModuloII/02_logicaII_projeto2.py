import json

def read_json_file(jsonfile):
    with open(jsonfile, 'r') as file:
        tables = json.loads(file.read())
        return tables

def write_jason_file(jsonfile):
    with open(jsonfile, 'w+', encoding='UTF-8') as file:
        file.write(json.dumps(musicians, indent=2))

def add_musician(email, name, genres, instruments, musicians):
    musicians.update({email: {'name': name, 'genres': genres.lower().split(), 'instruments': instruments.lower().split()}})
    return f'''
{100*'='}
Pessoa adicionada com sucesso!
{100*'='}
Email: {email}
Nome: {name}
Gêneros: {genres.title()}
Instrumentos: {instruments.title()}
{100*'='}

'''

def musician_search(s_values, search_type, musicians):
    l_names = [dict['name'] for dict in musicians.values()]
    l_emails = [dict for dict in musicians]
    l_genres = [dict['genres'] for dict in musicians.values()]
    l_instruments = [dict['instruments'] for dict in musicians.values()]
    all_listed = {'name': l_names, 'email': l_emails, 'genres': l_genres, 'instruments': l_instruments}

    field_search_dict = {}
    for k, v in s_values.items():
        for idx in range(len(all_listed[k])):
            if k not in field_search_dict.keys():
                field_search_dict[k] = [v in all_listed[k][idx]]
            else:
                field_search_dict[k].append(v in all_listed[k][idx])

    result_array = []
    for key in field_search_dict.keys():
        for idx in range(len(field_search_dict[key])):
            if idx == len(result_array):
                result_array.append([field_search_dict[key][idx]])
            else:
                result_array[idx].append(field_search_dict[key][idx])

    and_or_result_array = []
    for item in result_array:
        if search_type == '1':
            and_or_result_array.append(all(item))
        else:
            and_or_result_array.append(any(item))

    result_list = []

    for idx in range(len(and_or_result_array)):
        if and_or_result_array[idx]:
            artist_key = l_emails[idx]
            result_list.append({artist_key: musicians[artist_key]})

    en_pt_corr = {'name': 'nome', 'email': 'email', 'genres': 'gêneros', 'instruments': 'instrumentos'}

    message = f'{100*"="}\nForam localizados {str(len(result_list))} resultados que atendem aos critérios:\n'
    for k, v in s_values.items():
        message += f"{en_pt_corr[k]} = \'{v}\' {'E' if search_type == '1' else 'OU'} "
    message = (message[:-2] if search_type == '1' else message[:-3]) + '\n'
    for item in result_list:
        message += f'{100*"="}\n'
        for email, artist in item.items():
            message += f'email: {email}\n'
            for k, v in artist.items():
                message += f'{en_pt_corr[k].title()}: {", ".join(v) if type(v) == list else v}\n'
    message += f'{100*"="}\n'

    return message

def mod_musician(key_1, key_2, action, chg_val, musicians):
    musician = musicians[key_1]
    musician[key_2].append(chg_val) if action == '1' else musician[key_2].remove(chg_val)
    
    en_pt_corr = {'name': 'nome', 'email': 'email', 'genres': 'gêneros', 'instruments': 'instrumentos'}
    
    message = f'{100*"="}\nDados atualizados:\n'
    message += f'{100*"="}\n'
    message += f'email: {key_1}\n'
    for k, v in musician.items():
        message += f'{en_pt_corr[k].title()}: {", ".join(v) if type(v) == list else v}\n'
    return message

def form_group(grp_insts, grp_genre, musicians):

    genre_musicians = [{k:v} for k, v in musicians.items() for genre in v['genres'] if genre == grp_genre]

    inst_musicians = []
    try:
        for idx in range(len(grp_insts)):
            for musician in genre_musicians:
                for k, v in musician.items():
                    if grp_insts[idx] in v['instruments']:
                        if idx == len(inst_musicians):
                            inst_musicians.append([k])
                        else: inst_musicians[idx].append(k)
    except:
        return f'{100*"="}\nNão foi possível formar uma banda com os dados informados.\n'

    array_input_list = inst_musicians
    array_output_list = []
    array_len = 1
    for idx in range(len(array_input_list)):
        array_len *= len(array_input_list[idx])
    p_l_len = 1
    for idx in range(len(array_input_list)):
        inner_list = []
        l_len = len(array_input_list[idx])
        array_len /= l_len
        for item in array_input_list[idx]:
            temp_list = []
            temp_list.append(((item+' ')*int(array_len)).strip().split(' '))
            for item in temp_list:
                for sitem in item:
                    inner_list.append(sitem)
        array_output_list.append(p_l_len*inner_list)
        p_l_len *= l_len

    all_comb = []
    for item in array_output_list:
        for idx in range(len(item)):
            if idx == len(all_comb):
                all_comb.append([item[idx]])
            else:
                all_comb[idx].append(item[idx])

    same_ps_filtered = []   
    for item in all_comb:
        item = list(dict.fromkeys(item))
        if len(item) == len(grp_insts): same_ps_filtered.append(item)
    
    set_list = [{(person, inst) for person, inst in zip(combination, grp_insts)} for combination in same_ps_filtered]
    permut_filtered = []
    for item in set_list:
        if item not in permut_filtered:
            permut_filtered.append(item)

    comb_list = [list(item) for item in permut_filtered]
    text_list = []    
    for comb in comb_list:
        group_str = ''
        for musician in comb:
            group_str += f'({musician[0]}, {musician[1]}) + '
        text_list.append(group_str[:-3])


    if len(comb_list) == 0:
        message = '\nNão foi possível formar uma banda com os dados informados.\n'
    else:
        message = f'\nCom os dados informados, foi possível formar {str(len(comb_list))} combinações diferentes de bandas.\n'
        for idx in range(len(text_list)):
            f'{100*"="}\n'
            message += f'{(idx+1):03d}. {text_list[idx]}\n'

    return message

def im1_check_term(term, term_type):
    if term_type == 'name':
        try:
            if all(char.isalpha() or char == ' ' for char in term):
                return term
            else:
                raise Exception
        except:
            print('Utilize apenas letras ou espaço.')
            return im1_check_term(input('Informe corretamente o nome da pessoa: '), 'name')
    elif term_type == 'email':
        try:
            if not all(char.isdigit() or char in list('_-.@') for char in term):
                pass
            else:
                print('O email informado contém caracteres inválidos.')
                raise Exception
            if len([char for char in term if char == '@']) == 1:
                pass
            else:
                print('O email informado deve conter necessariamente e apenas uma \'@\'.')
                raise Exception
            if term.lower() not in musicians.keys():
                return term
            else:
                print('Já existe pessoa cadastrada com o email informado.')
                raise Exception
        except:
            return im1_check_term(input('Informe novamente um email: '), 'email')
    elif term_type == 'genres':
        try:
            if all(char.isdigit() or char in list(', -') for char in term):
                return term
            else:
                print('Utilize apenas letras e espaço, separe os gêneros por vírgula.')
                raise Exception
        except:
            return im1_check_term(input('Informe novamente um email: '), 'gen_inst')
    
def im1_check_term(term, term_type):
    if term_type == 'name':
        try:
            if all(char.isalpha() or char == ' ' for char in term) and len(term) > 0:
                return term
            else:
                raise Exception
        except:
            print('Utilize apenas letras ou espaço.')
            return im1_check_term(input('Informe corretamente o nome da pessoa: '), 'name')
    elif term_type == 'email':
        try:
            if all(char.isalnum() or char in list('_-.@') for char in term):
                pass
            else:
                print('O email informado contém caracteres inválidos.')
                raise Exception
            if len([char for char in term if char == '@']) == 1:
                pass
            else:
                print('O email informado deve conter necessariamente e apenas uma \'@\'.')
                raise Exception
            if term not in musicians.keys():
                return term
            else:
                print('Já existe pessoa cadastrada com o email informado.')
                raise Exception
        except:
            return im1_check_term(input('Informe novamente um email: '), 'email')
    elif term_type == 'gen_inst':
        try:
            if all(char.isalpha() or char in list(', -') for char in term) and len(term) > 0 and len([char for char in term if char.isalpha()]) > 0:
                return term
            else:
                print('Utilize apenas letras e espaço, separe os gêneros por vírgula.')
                raise Exception
        except:
            return im1_check_term(input('Informe novamente um termo: '), 'gen_inst')

def input_menu_1(musicians):
    email = im1_check_term(input('Informe o email da pessoa: '), 'email')
    name = im1_check_term(input('Informe o nome da pessoa: '), 'name')
    genres = im1_check_term(input('Informe os gêneros musicais da pessoa: '), 'gen_inst')
    instruments = im1_check_term(input('Informe os instrumentos da pessoa: '), 'gen_inst')
    return add_musician(email, name, genres, instruments, musicians)

def im2_check_key(key, options, moment='inicial'):
    if moment == 'inicial':
        while key not in options:
            key = im2_check_key(input(f'Opção não existe, informe o campo de busca desejado ({"/".join(options.keys())}): '), options)
        if key == '9': key = im2_check_key(input(f'É necessário informar ao menos um campo, informe o campo de busca desejado ({"/".join(options.keys())}): '), options)
    if moment == 'demais':
        while key not in options:
            key = input(f'Opção não existe, informe o campo de busca desejado ({"/".join(options.keys())}): ')
    return key

def input_menu_2(musicians):
    options = {'1': 'nome', '2': 'email', '3': 'gêneros', '4': 'instrumentos', '9': 'continuar', '0': 'voltar ao menu inicial'}
    e_opt = {'1': 'name', '2': 'email', '3': 'genres', '4': 'instruments'}
    search_type_opt = {'1': 'E', '2': 'OU'}
    print(f'\n','Opções disponíveis:', sep='')
    for idx in list(options):
        print(f'{idx}. {options[str(idx)].capitalize()}')
    print(f'\n{100*"="}')

    key = ''
    while key not in list('123490'):
        key = im2_check_key(input(f'Informe o campo de busca desejado ({"/".join(options.keys())}): '), options)
        value = input(f'Informe o valor que deseja buscar para \'{options[key]}\': ')
        s_values = {e_opt[key]: value}
        options.pop(key)
        
    while len(options)>2:
        key = im2_check_key(input(f'Informe um campo adicional de busca ou escolha continuar ({"/".join(options.keys())}): '), options, 'demais')
        if key == '9': break
        elif key == '0': main_menu(musicians)
        else:
            value = input(f'Informe o valor que deseja buscar para \'{options[key]}\': ')
            s_values.update({e_opt[key]: value})
            options.pop(key)
    search_type = input(f'Informe uma forma de busca \'1\': \'E\', \'2\': \'OU\' ({"/".join(search_type_opt.keys())}): ') if len(s_values) > 1 else '1'
    while search_type not in search_type_opt:
        search_type = input(f'Opção inválida, informe uma forma de busca \'1\': \'E\', \'2\': \'OU\' ({"/".join(search_type_opt.keys())}): ')
    
    return musician_search(s_values, search_type, musicians)

def input_menu_3(musicians):
    fld_opt = {'1': 'gêneros', '2': 'instrumentos'}
    e_fld_opt = {'1': 'genres', '2': 'instruments'}
    key_1 = input('Informe o email da pessoa que deseja alterar: ')
    while key_1 not in musicians:
        key_1 = input('Email não encontrado, informe o email da pessoa que deseja alterar: ')
    key_2 = input('Informe o campo que deseja alterar, \'1\': gêneros ou \'2\': instrumentos (1/2): ')
    while key_2 not in fld_opt:
        key_2 = input('Opção inválida, informe o campo que deseja alterar, \'1\': gêneros ou \'2\': instrumentos (1/2): ')
    fld_sing = fld_opt[key_2][:-1] 
    print(f'Foram localizados os seguintes {fld_opt[key_2]}:\n{", ".join(list(musicians[key_1][e_fld_opt[key_2]]))}')
    action = input(f'Escolha \'1\': Adicionar {fld_sing} ou \'2\': Remover {fld_sing} (1/2): ')
    while action not in list('12'):
        action = input(f'Opção inválida, escolha \'1\': Adicionar {fld_sing} ou \'2\': Remover {fld_sing} (1/2): ')
    chg_val = input(f'Informe o {fld_sing} que deseja {"adicionar" if action == "1" else "remover"}: ')
    if action == '1':
        while chg_val in list(musicians[key_1][e_fld_opt[key_2]]):
            chg_val = input(f'{fld_sing.capitalize()} já está cadastrado, informe o {fld_sing} que deseja adicionar: ')
    else:
        while chg_val not in list(musicians[key_1][e_fld_opt[key_2]]):
            chg_val = input(f'{fld_sing.capitalize()} não encontrado, informe o {fld_sing} que deseja remover: ')
    
    key_2 = e_fld_opt[key_2]
    return mod_musician(key_1, key_2, action, chg_val, musicians)

def im4_check_n_members(num_of_members):
    try:
        num_of_members = int(num_of_members)
        if num_of_members > 1:
            return num_of_members
        else:
            print('Número de integrantes inválido, deve ser maior do que 1.')
            raise Exception
    except:
        num_of_members = input("Opção inválida. Informe o número de integrantes que deseja na banda: ")
        return im4_check_n_members(num_of_members)

def im4_check_insts(instrument):
    try:
        inst_in_list = instrument in [item for musician in musicians.values() for item in musician['instruments']]
        if inst_in_list:
            return instrument
        else:
            raise Exception
    except:
        return im4_check_insts(input("Opção inválida. Informe um instrumento válido: "))

def im4_check_genre(grp_genre):
    try:
        gre_in_list = grp_genre in [item for musician in musicians.values() for item in musician['genres']]
        if gre_in_list:
            return grp_genre
        else:
            raise Exception
    except:
        return im4_check_genre(input("Opção inválida. Informe um gênero válido: "))

def input_menu_4(musicians):
    num_of_members = im4_check_n_members(input(f'Informe o número de integrantes que deseja na banda: '))
    grp_insts = []
    while len(grp_insts) < num_of_members:
        instrument = im4_check_insts(input(f'Informe o instrumento do integrante nro {len(grp_insts)+1}: '))
        grp_insts.append(instrument)
    grp_genre = im4_check_genre(input(f'Informe o gênero musical da banda a ser formada: '))

    return form_group(grp_insts, grp_genre, musicians)

def get_option(options):
    print(f"{100*'='}\n",
        'MENU PRINCIPAL\n',
        f"{100*'='}\n",
        'Informe a opção desejada:', sep="")
    for idx in range(len(options)):
        print(f'{idx+1}. {options[str(idx+1)][1]}')
    print('0. Sair\n', 
        f"{100*'='}", sep='')

    return input()

def main_menu(musicians):
    options = {
        "1": [input_menu_1, 'Cadastrar nova pessoa'],
        "2": [input_menu_2, 'Buscar pessoas'],
        "3": [input_menu_3, 'Modificar uma pessoa'],
        "4": [input_menu_4, 'Montar bandas']
    }

    option = get_option(options)
    
    while option != "0":
        if option not in options and option != "0":
            print(f'\nVocê digitou: {option}\n',
            'Opção inválida!\n', sep='')
            option = get_option(options)
            continue

        else:
            print(f'\n{100*"="}\n',
            f'Opção selecionada: {options[option][1]}\n',
            f'{100*"="}', sep='')
            message = options[option][0](musicians)
            print(message)

        option = get_option(options)
    else:
        write_jason_file(outfile)
        print(f"\n\n{100*'='}\nArquivo \'{outfile}\' gravado com sucesso!\nObrigado por usar o programa!\n{100*'='}\n",)

def chk_db_len(db_len, tt_len):
    try:
        int(db_len)
        not 1 < int(db_len) < tt_len
        return db_len
    except:
        return chk_db_len(input('Digite um valor válido: '))

def load_menu(filename):
    print(f"\n\n{100*'='}\n",
        'Bem vindo ao programa formador de bandas!\n',
        f"{100*'='}\n\n",sep='')
    try:
        musicians = read_json_file(filename)
        print(f'Base \'{filename}\' encontrada, com {len(musicians)} pessoas cadastradas.\n{100*"="}')
        use_db = input('Gostaria de utilizá-la? [\'1\': Sim] ou [\'Não\'] (1/2): ')
        while use_db not in list('12'):
            use_db = input(f'Não entendi. Gostaria de utilizar a base {filename}?\n[\'1\': Sim] ou [\'Não\'] (1/2): ')
        if use_db == '1':
            db_len = chk_db_len(input(f'Informe quantas pessoas da base gostaria de usar (máx. {len(musicians)}): '), len(musicians))
            musician_list = [{k: v} for k, v in musicians.items()][:int(db_len)]
            musicians = {}
            for item in musician_list: musicians.update(item)
            print(f"{100*'='}\n",
                'Base carregada com sucesso!\n',
                f"{100*'='}\n\n", sep='')
            return musicians
        else:
            print(f"{100*'='}\n",
            'Nova base iniciada!\n',
            f"{100*'='}\n\n", sep='')
            return {}
    except:
        print(f"{100*'='}\n",
        'Não foi localizada uma base de dados.\n',
        'Nova base iniciada!\n',
        f"{100*'='}\n\n", sep='')
        return {}
        
filename = 'musicians_v01_dict_letscode.json'
outfile = 'musicians_v01_dict_letscode_output.json'
musicians = load_menu(filename)
main_menu(musicians)