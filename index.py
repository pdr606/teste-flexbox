import bisect

dado = {}
bcdados = []
contador = 0

def cadastrar_funcionario(id):
    global contador
    global dado
    global bcdados
    while True:
        print('\033[7;30;43m-------------------- MENU CADASTRAR FUNCIONÁRIO --------\033[0;0m')
        contador += 1
        print(f'Código do Funcionário = {contador}')
        dado['Código Funcionário'] = contador
        dado['Nome'] = str(input('Nome: '))
        dado['Setor'] = input('Setor: ').strip()
        dado['Salário'] = float(input('Salário: R$'))
        bcdados.append(dado.copy())
        print(f'\033[32mFuncionário {contador} cadastrado com sucesso\033[0;0m')
        break

def consultar_funcionario():
    while True:
        print('\033[7;30;47m-------------------- MENU CONSULTAR FUNCIONÁRIO --------\033[0;0m')
        print('Escolha a opção desejada: ')
        print('1 - Consultar Todos os Funcionários\n'
              '2 - Consultar Funcionários por ID\n'
              '3 - Consultar Funcionários por SETOR\n'
              '4 - Retornar')
        opcao_consulta = int(input('>>'))
        if opcao_consulta == 1:
            for e in bcdados:
                for i, j in e.items():
                    print(f'{i}: {j}')
        if opcao_consulta == 2:
            while True:
                opcao_id = int(input('Digite o ID do funcionário: '))
                status = False
                if opcao_id > 0 and opcao_id <= contador:
                    for e in bcdados:
                        for i, j in e.items():
                            if e['Código Funcionário'] == opcao_id:
                                print(f'{i}: {j}')
                                status = True
                            else:
                                status = False
                if status == False:
                    print('\033[1;31mID inválido ou apagado\033[0;0m')
                else:
                    print('\033[1;31mID inválido\033[0;0m')
                break
        if opcao_consulta == 3:
            opcao_setor = str(input('Digite o SETOR do funcionário(a): ')).strip()
            for e in bcdados:
                for i, j in e.items():
                    if e['Setor'] == opcao_setor:
                        print(f'{i}: {j}')
        if opcao_consulta == 4:
            break
        if opcao_consulta > 4:
            print('\033[1;31mOpção Inválida\033[0;0m')

def remover_funcionario():
    while True:
        print('\033[7;30;41m-------------------- MENU REMOVER FUNCIONÁRIO --------\033[0;0m')
        opcao_deletar = int(input('Digite o ID do funcionário que deseja deletar: '))
        if opcao_deletar > 0 and opcao_deletar <= contador:
            for produto in bcdados:
                if produto['Código Funcionário'] == opcao_deletar:
                    bcdados.remove(produto)
                    print(f'\033[32mFuncionário {opcao_deletar} deletado com sucesso\033[0;0m')
            break
        else:
            print('\033[1;31mID inválido, tente novamente\033[0;0m')
            continue






def menu_principal():
    while True:
        print('\033[7;30;46m-------------------- MENU PRINCIPAL --------------------\033[0;0m')
        print('Escolha a opção desejada: ')
        print('1 - Cadastrar Funcionário\n'
              '2 - Consultar Funcionários(s)\n'
              '3 - Remover Funcionário\n'
              '4 - Sair')
        opcao_usuario = int(input('>>'))
        if opcao_usuario == 1:
            cadastrar_funcionario(0)
        if opcao_usuario == 2:
            consultar_funcionario()
        if opcao_usuario == 3:
            remover_funcionario()
        if opcao_usuario == 4:
            break
        if opcao_usuario > 4:
            print('\033[1;31mOpção Inválida\033[0;0m')
    print('-' *30)


menu_principal()
print('Obrigado por usar o meu programa até aqui :) ')