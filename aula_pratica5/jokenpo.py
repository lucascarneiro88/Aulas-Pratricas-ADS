import random

# Inicialização das variáveis globais
vencedor1 = 0
vencedor2 = 0
empate = 0

# Função para validar entrada inteira
def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while (x < min) or (x > max):
        x = int(input(pergunta))
    return x

# Função para definir vencedor
def vencedor(jogador1, jogador2_computador):
    global vencedor1, vencedor2, empate
    if jogador1 == 1:  # Pedra
        if jogador2_computador == 1:  # Pedra
            empate += 1
        elif jogador2_computador == 2:  # Papel
            vencedor2 += 1
        elif jogador2_computador == 3:  # Tesoura
            vencedor1 += 1
    elif jogador1 == 2:  # Papel
        if jogador2_computador == 1:  # Pedra
            vencedor1 += 1
        elif jogador2_computador == 2:  # Papel
            empate += 1
        elif jogador2_computador == 3:  # Tesoura
            vencedor2 += 1
    elif jogador1 == 3:  # Tesoura
        if jogador2_computador == 1:  # Pedra
            vencedor2 += 1
        elif jogador2_computador == 2:  # Papel
            vencedor1 += 1
        elif jogador2_computador == 3:  # Tesoura
            empate += 1
    resultados = [vencedor1, vencedor2, empate]
    return resultados

# Programa principal
print('JOKENPO')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')

jogadas = []
resultados = []

while True:
    jogador1 = valida_int('Escolha sua jogada (1-3, 0 para sair):', 0, 3)
    if jogador1 == 0:
        break

    jogador2_computador = random.randint(1, 3)  # Gera um número aleatório entre 1 e 3 para a jogada do computador
    jogadas.append([jogador1, jogador2_computador])
    resultados = vencedor(jogador1, jogador2_computador)

# Mostrar resultados das jogadas
for jogada in jogadas:
    jogador1, jogador2_computador = jogada
    resultado = "Empate" if jogador1 == jogador2_computador else "Jogador 1" if (jogador1 == 1 and jogador2_computador == 3) or (jogador1 == 2 and jogador2_computador == 1) or (jogador1 == 3 and jogador2_computador == 2) else "Computador"
    jogada_str = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}
    print(f'Jogador 1: {jogada_str[jogador1]} - Computador: {jogada_str[jogador2_computador]} -> {resultado}')

# Mostrar contagem de vitórias e empates
print(f'Número de vitórias do Jogador 1: {resultados[0]}')
print(f'Número de vitórias do Computador: {resultados[1]}')
print(f'Número de empates: {resultados[2]}')
