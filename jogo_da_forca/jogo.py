import desenhos as d
import fileHandler as fH
from random import choice

def jogar():
    lista_palavras = []
    arquivo = fH.abrir_arquivo_leitura('palavras.txt')
    if arquivo:
        for linha in arquivo:
            palavra = linha.strip()
            lista_palavras.append(palavra)
        palavra_sorteada = choice(lista_palavras)
    else:
        print("Erro ao abrir o arquivo de palavras.")

    for _ in range(50):  # para dar espaço para melhor experiência de jogo
        print()

    digitadas = []
    acertos = []
    erros = 0  # corrigido para ser um inteiro

    nome = input('Quem está jogando? ')

    while True:
        adivinha = d.imprimir_palavra_secreta(palavra_sorteada, acertos)

        # Condição de vitória
        if adivinha == palavra_sorteada:
            print('Você acertou!')
            break

        # Tentativas
        tentativa = input('\nDigite uma letra: ').lower().strip()
        if tentativa in digitadas:
            print('Você já usou esta letra!')
            continue
        else:
            digitadas.append(tentativa)  # ou append
            if tentativa in palavra_sorteada:
                acertos.append(tentativa)
            else:
                erros += 1
                print('Você errou!')

        score = d.desenhar_forca(erros)

        # Condição de fim de jogo
        if erros == 6:
            print('Enforcado pela inquisição das letras')
            print(f'A palavra secreta era {palavra_sorteada}.')
            break

        fH.inserir_score('score.txt', nome, score)

