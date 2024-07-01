import os
import jogo as j
import fileHandler as fH

def mostrar_menu():
    print('='*30)
    print('\n1 - JOGAR')
    print('2 - SCORE')
    print('3 - SAIR\n')
    print('='*30)

arquivo = 'score.txt'

# Verifica se o arquivo existe
if not os.path.isfile(arquivo):
    print('Arquivo não existe')
    # Cria o arquivo apenas abrindo-o em modo de escrita
    with open(arquivo, 'w') as f:
        pass  # Nada precisa ser escrito, apenas cria o arquivo vazio
else:
    print('Arquivo localizado, já existe')

while True:
    mostrar_menu()
    opcao = int(input('ESCOLHA UMA OPÇÃO (1/2/3):'))

    if opcao == 1:
        print('Iniciar jogo')
        j.jogar()  # chama função jogar
    elif opcao == 2:
        print('SCORE')
    elif opcao == 3:
        print('Saindo do jogo.')
        break
    else:
        print('Opção inválida')
