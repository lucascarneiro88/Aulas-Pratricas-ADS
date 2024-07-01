import os

def abrir_arquivo_leitura(nome):
    try:
        arquivo = open(nome, 'r')
        return arquivo
    except FileNotFoundError:
        return None

def inserir_score(nome_arquivo, nome_jogador, score):
    with open(nome_arquivo, 'a') as arquivo:
        arquivo.write(f'{nome_jogador}: {score}\n')
