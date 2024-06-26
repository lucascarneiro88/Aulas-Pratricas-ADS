palavras = ('Banana', 'Skate', 'Arroz', 'Batata')

for palavra in palavras:
    print(f'\nPalavra: {palavra.upper()}. vogais:')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end='')
