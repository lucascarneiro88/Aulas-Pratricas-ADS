# Exigencia 1 de 8
print('Bem vindos a empresa do Lucas Carneiro')

# Exigencia 2 de 8
listaFuncionarios = []  # lista se inicia vazia p/ ser salvo os cadastros 
idGlobal = 4872694  # id para indentificar cada cadastro feito / na função cadastro vai somar + 1 ao id para cada novo cadastro


# Exigencia 3 de 8
# Função cadastro de funcionarios passando o id 
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
    listaFuncionarios.append(funcionario.copy())


# Exigencia 4 de 8
# Função consulta de funcionarios
def consultarFuncionarios():
    while True:
        opcao = int(input('Consultar Funcionários\n 1 - Consultar Todos\n 2 - Consultar por ID\n 3 - Consultar por Setor\n 4 - Retornar ao Menu\n Escolha uma Opção: '))
        if opcao == 1:
            for funcionario in listaFuncionarios:
                print(f"ID: {funcionario['id']}")
                print(f"NOME: {funcionario['nome']}")
                print(f"SALÁRIO: R${funcionario['salario']:.2f}")
                print(f"SETOR: {funcionario['setor']}")
                print("-" * 30)
        elif opcao == 2:
            idConsulta = int(input('Digite o Id do funcionário: '))
            encontrado = False
            for funcionario in listaFuncionarios:
                if funcionario['id'] == idConsulta:
                    print(f"ID: {funcionario['id']}")
                    print(f"NOME: {funcionario['nome']}")
                    print(f"SALÁRIO: R${funcionario['salario']:.2f}")
                    print(f"SETOR: {funcionario['setor']}")
                    print("-" * 30)
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
                print(f'Não há funcionários no setor {setorConsulta}.')
        elif opcao == 4:
            return
        else:
            print('Opção inválida')

# Exigencia 5 de 8
# Função para remover funcionario pelo id 
def removerFuncionario():
    while True:
        id_remover = int(input('Digite o id do funcionário a ser removido: '))
        encontrado = False
        for funcionario in listaFuncionarios:
            if funcionario['id'] == id_remover:
                listaFuncionarios.remove(funcionario)
                print(f'Funcionário de id {id_remover} removido com sucesso.')
                encontrado = True
                break
        if encontrado:
            break  # Sair do loop apenas se o funcionário foi encontrado e removido
        else:
            print('ID inválido')


# Função para encerrar programa
def encerrarPrograma():
    print('Programa encerrado.')
    exit()


# Exigencia 6 de 8
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
