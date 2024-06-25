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
    while True:
        try:
            x = int(input(pergunta))
            if min <= x <= max:
                return x
            else:
                print(f"Por favor, insira um número entre {min} e {max}.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro.")

def existeArquivo(nomeArquivo):
    """
    Função para verificar se arquivo existe, com parâmetro nome do arquivo.
    
    Args:
        nomeArquivo (str): Nome do arquivo a ser verificado.
    
    Returns:
        bool: True se o arquivo existe, False caso contrário.
    """
    try:
        with open(nomeArquivo, 'rt'):
            pass
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nomeArquivo):
    """
    Função para criar arquivo com parâmetro recebido o nome do arquivo.
    
    Args:
        nomeArquivo (str): Nome do arquivo a ser criado.
    """
    try:
        with open(nomeArquivo, 'wt+'):
            pass
    except:
        print('Erro ao criar arquivo.')
    else:
        print(f'Arquivo {nomeArquivo} criado com sucesso!\n')

def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    """
    Função para cadastrar jogo.
    
    Args:
        nomeArquivo (str): Nome do arquivo onde os dados serão cadastrados.
        nomeJogo (str): Nome do jogo a ser cadastrado.
        nomeVideogame (str): Nome do videogame a ser cadastrado.
    """
    try:
        with open(nomeArquivo, 'at') as a:
            a.write(f'{nomeJogo};{nomeVideogame}\n')
    except:
        print('Erro ao abrir arquivo')

def listarArquivo(nomeArquivo):
    """
    Função para listar arquivo.
    
    Args:
        nomeArquivo (str): Nome do arquivo a ser listado.
    """
    try:
        with open(nomeArquivo, 'rt') as a:
            print("Listagem dos Jogos Cadastrados:")
            for linha in a:
                nomeJogo, nomeVideogame = linha.strip().split(';')
                print(f"Nome do Jogo: {nomeJogo}\nNome do Videogame: {nomeVideogame}\n")
    except:
        print('Erro ao ler arquivo.')

def main():
    """
    Função principal que controla o fluxo do programa.
    """
    arquivo = 'games.txt'
    
    if existeArquivo(arquivo):
        print('Arquivo localizado já existente')
    else:
        print('Arquivo inexistente')
        criarArquivo(arquivo)
    
    while True:
        print('MENU')
        print('1 - Cadastrar novo item')
        print('2 - Listar cadastros')
        print('3 - Sair')

        operacao = valida_int('Escolha a opção desejada (1-3): ', 1, 3)
        
        if operacao == 1:
            print('Opção de cadastrar novo item selecionada...\n')
            nomeJogo = input('Nome do jogo: ')
            nomeVideogame = input('Nome do videogame: ')
            cadastrarJogo(arquivo, nomeJogo, nomeVideogame)
        elif operacao == 2:
            print('Opção de listar todos cadastros selecionada...\n')
            listarArquivo(arquivo)
        elif operacao == 3:
            print('Encerrando o programa')
            break

if __name__ == '__main__':
    main()

# garante que a função main()
# seja chamada apenas quando o script jogos2.0.py 
# for executado diretamente.