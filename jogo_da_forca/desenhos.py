def imprimir_palavra_secreta(palavra, acertos):
    adivinha = ''
    for letra in palavra:
        if letra in acertos:
            adivinha += letra + ' '  # Adiciona um espaço após cada letra adivinhada
        else:
            adivinha += '\u2588 '  # Adiciona um bloco Unicode (espaço) para letras não adivinhadas
    print(f'ADIVINHE ({len(palavra)} letras):')
    print(adivinha)
    return adivinha.replace(' ', '')  # Remove os espaços para retornar a palavra adivinhada sem espaços


def desenhar_forca(erros):
    score = 1000

    print('x==:==')
    print('x  :  ')
    if erros >= 1:
        print('x 0 ')
        score = 800
    else:
        print('x')

    linha2 = ''
    if erros == 2:
        linha2 = ' | '
        score = 600
    elif erros == 3:
        linha2 = '/| '
        score = 400
    elif erros >= 4:
        linha2 = ' /|\\ '
        score = 200
    print(f'x{linha2}')

    linha3 = ''
    if erros == 5:
        linha3 += ' / '
        score = 100
    elif erros >= 6:
        linha3 += ' / \\ '
        score = 0
    print(f'x{linha3}')

    print('x\n======')

    return score
