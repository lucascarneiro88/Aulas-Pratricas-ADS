print('Bem-vindo ao CineMegan')  # Exibe uma mensagem de boas-vindas

# Inicializa as variáveis para rastrear o total de pessoas, o dinheiro arrecadado e a soma das idades
total = 0  # Quantidade total de pessoas
dinheiro = 0  # Quantidade total de dinheiro arrecadado
acumulado_idades = 0  # Soma de todas as idades para calcular a média

# Loop para processar a entrada de idade dos usuários
while True:
    try:
        # Solicita a idade do usuário e converte para inteiro
        idade = int(input('Qual sua idade? '))
    except ValueError:
        # Tratamento de erro caso a entrada não seja um número válido
        print("Por favor, insira uma idade válida.")
        continue  # Retorna ao início do loop para solicitar a idade novamente

    if idade == 0:
        break  # Interrompe o loop se a idade for 0, indicando o fim das entradas

    total += 1  # Incrementa o contador de pessoas
    acumulado_idades += idade  # Adiciona a idade fornecida ao acumulado de idades

    # Determina o preço do ingresso com base na idade
    if idade <= 3:
        ingresso = 0  # Ingresso gratuito para crianças de 3 anos ou menos
    elif idade > 12:
        ingresso = 30  # Ingresso de R$ 30,00 para pessoas com mais de 12 anos
    else:
        ingresso = 15  # Ingresso de R$ 15,00 para pessoas entre 4 e 12 anos

    dinheiro += ingresso  # Adiciona o valor do ingresso ao total de dinheiro arrecadado

# Verifica se houve entradas válidas (pelo menos uma pessoa)
if total > 0:
    # Calcula a média de idade
    media_idade = acumulado_idades / total
    # Exibe o total de pessoas, o total arrecadado e a média de idade
    print(f'Total de pessoas: {total}')
    print(f'Total arrecadado: R$ {dinheiro}')
    print(f'Média de idade: {media_idade:.2f}')
else:
    # Mensagem para o caso de nenhuma idade válida ter sido fornecida
    print('Nenhuma idade válida foi fornecida.')






# print('Bem vindo ao CineMegan')
# total = 0 # total de pessoas inicializa em 0, vazio, para saber quantidade de pessoas
# dinheiro = 0  # total dinheiro inicializa em 0, vazio , para saber quanto arrecadou
# acumulado_idades = 0

# while True:
#    idade = int(input('Qual sua idade?'))
#    if idade == 0:
#       break
   
#    total += 1
#    acumulado_idades += idade

#    if idade <= 3:
#       ingresso = 0
#    else:
#       if idade > 12:
#          ingresso = 30
#       else:
#          ingresso = 15


#       dinheiro += ingresso

# if total > 0:
#    media = idade / total
#    print(f'Total de pessoas: {total}')
#    print(f'Total arrecadado: {total}')
#    print(f'Média arecadada: {total}')

# else:
#    if total <= 0:
#       print('Isso não configura uma idade, ai você me quebra eu')

         