# Exibição inicial
print('Bem vindos a empresa do Lucas Carneiro')

# Lista vazia para armazenar os funcionários
listaFuncionarios = []

# Utilizando o RU como identificador global inicial
idGlobal = 4872694  # Substitua pelo seu RU convertido para inteiro

# Função para cadastrar funcionários
def cadastroDeFuncionarios(id):
    nome = input('Digite o nome do funcionário: ')
    setor = input('Digite o setor do funcionário: ')
    salario = float(input('Digite o salário do funcionário: '))

    funcionario = {
        'id': id,
        'nome': nome,
        'setor': setor,
        'salario': salario
    }
    listaFuncionarios.append(funcionario.copy())  # Adiciona uma cópia do funcionário à lista

# Função para consultar funcionários
def consultarFuncionarios():
    while True:
        opcao = int(input('Consultar Funcionários\n 1 - Consultar Todos\n 2 - Consultar por ID\n 3 - Consultar por Setor\n 4 - Retornar ao Menu\n Escolha uma Opção: '))
        if opcao == 1:
            print("Todos os funcionários:")
            for funcionario in listaFuncionarios:
                print(f"ID: {funcionario['id']}")
                print(f"NOME: {funcionario['nome']}")
                print(f"SALÁRIO: R${funcionario['salario']:.2f}")
                print(f"SETOR: {funcionario['setor']}")
                print("-" * 30)
        elif opcao == 2:
            id_consulta = int(input('Digite o ID do funcionário (seu RU): '))
            encontrado = False
            for funcionario in listaFuncionarios:
                if funcionario['id'] == id_consulta:
                    print(f"ID: {funcionario['id']}")
                    print(f"NOME: {funcionario['nome']}")
                    print(f"SALÁRIO: R${funcionario['salario']:.2f}")
                    print(f"SETOR: {funcionario['setor']}")
                    encontrado = True
                    break
            if not encontrado:
                print('Funcionário não encontrado.')
        elif opcao == 3:
            setorConsulta = input('Digite o setor: ')
            encontrados = False
            for funcionario in listaFuncionarios:
                if funcionario['setor'] == setorConsulta:
                    print(f"ID: {funcionario['id']}")
                    print(f"NOME: {funcionario['nome']}")
                    print(f"SALÁRIO: R${funcionario['salario']:.2f}")
                    print(f"SETOR: {funcionario['setor']}")
                    print("-" * 30)
                    encontrados = True
            if not encontrados:
                print('Nenhum funcionário encontrado neste setor.')
        elif opcao == 4:
            return
        else:
            print('Opção inválida')

# Função para remover funcionário por ID
def removerFuncionario():
    id_remover = int(input('Digite o ID do funcionário a ser removido (seu RU): '))
    encontrado = False
    for funcionario in listaFuncionarios:
        if funcionario['id'] == id_remover:
            listaFuncionarios.remove(funcionario)
            print(f'Funcionário de ID {id_remover} removido com sucesso.')
            encontrado = True
            break
    if not encontrado:
        print('ID inválido. Funcionário não encontrado.')

# Função para encerrar o programa
def encerrarPrograma():
    print('Programa encerrado.')
    exit()

# Menu principal
while True:
    opcao = int(input('Menu Principal:\n 1 - Cadastrar Funcionário\n 2 - Consultar Funcionário\n 3 - Remover Funcionário\n 4 - Encerrar Programa\n Escolha uma opção: '))
    if opcao == 1:
        idGlobal += 1
        cadastroDeFuncionarios(idGlobal)
    elif opcao == 2:
        consultarFuncionarios()
    elif opcao == 3:
        removerFuncionario()
    elif opcao == 4:
        encerrarPrograma()
    else:
        print('Opção inválida')
