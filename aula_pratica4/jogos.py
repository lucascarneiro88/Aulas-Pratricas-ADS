# Função para validar a entrada de um número inteiro dentro de um intervalo especificado
def valida_int(pergunta, min, max):
    """
    Função que valida a entrada de um número inteiro dentro de um intervalo especificado.

    Args:
        pergunta (str): A pergunta a ser exibida para o usuário solicitar a entrada.
        min (int): O valor mínimo aceitável para a entrada.
        max (int): O valor máximo aceitável para a entrada.

    Returns:
        int: Um número inteiro que está dentro do intervalo [min, max].
    """
    x = int(input(pergunta))
    while (x < min) or (x > max):
        x = int(input(pergunta))
    return x

# Função para verificar se arquivo existe, com parâmetro nome do arquivo
def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')  # abrindo arquivo
        a.close()  # fechando arquivo
    except FileNotFoundError:
        return False
    else:
        return True

# Função para criar arquivo com parâmetro recebido o nome do arquivo = nomeArquivo
def criarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')  # abrindo arquivo limpo para criar wt
        a.close()
    except:
        print('Erro ao criar arquivo.')
    else:
        print(f'Arquivo {nomeArquivo} criado com sucesso!\n')

# Função para cadastrar jogo
def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo, 'at')  # abre o arquivo para escrita e mantém o que já tem dentro dele (arquivo) -- at
        a.write(f'{nomeJogo}; {nomeVideogame}\n')  # abre arquivo para escrita -- write
    except:
        print('Erro ao abrir arquivo')
    finally:
        a.close()  # fechando arquivo 

# Função para listar arquivo
def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        print(a.read())
    except:
        print('Erro ao ler arquivo.')
    finally:
        a.close()

# Programa principal
arquivo = 'games.txt'  # simula um arquivo 
if existeArquivo(arquivo):  # verifica se arquivo é null, se null cria arquivo, se não arquivo já está criado
    print('Arquivo localizado já existente')
else:
    print('Arquivo inexistente')  # Se arquivo não existe, cria o arquivo
    criarArquivo(arquivo)  # cria arquivo com parâmetro passado arquivo

# Menu infinito para escolha
while True:
    print('MENU')
    print('1 - Cadastrar novo item')
    print('2 - Listar cadastros')
    print('3 - Sair')

    # Pergunta qual a opção o usuário quer escolher
    operacao = valida_int('Escolha a opção desejada (1-3): ', 1, 3)
    if operacao == 1:  # Novo item
        print('Opção de cadastrar novo item selecionada...\n')  # \n para quebra de linha
        nomeJogo = input('Nome do jogo: ')
        nomeVideogame = input('Nome do videogame: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)
    elif operacao == 2:  # Listar cadastros
        print('Opção de listar todos cadastros selecionada...\n')
        listarArquivo(arquivo)
    elif operacao == 3:  # Sair e encerrar programa
        print('Encerrando o programa')
        break
