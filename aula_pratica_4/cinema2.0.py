print('Bem-vindo ao CineMegan')  # Exibe uma mensagem de boas-vindas

# Solicita o número de pessoas que irão ao cinema
num_pessoas = int(input('Quantas pessoas irão ao cinema? '))

# Inicializa as variáveis para rastrear o total de pessoas, o dinheiro arrecadado e o relatório de custos por idade
total_pessoas = 0  # Quantidade total de pessoas
total_dinheiro = 0  # Quantidade total de dinheiro arrecadado
custos_por_idade = {'0-3': 0, '4-12': 0, '13+': 0}  # Dicionário para armazenar os custos por faixa etária

# Loop para processar a entrada de idade dos usuários
for i in range(num_pessoas):
    while True:
        try:
            # Solicita a idade do usuário e converte para inteiro
            idade = int(input(f'Qual a idade da pessoa {i+1}? '))
            break  # Sai do loop interno se a entrada for válida
        except ValueError:
            # Tratamento de erro caso a entrada não seja um número válido
            print("Por favor, insira uma idade válida.")

    # Determina o preço do ingresso com base na idade
    if idade <= 3:
        ingresso = 0  # Ingresso gratuito para crianças de 3 anos ou menos
        faixa_etaria = '0-3'
    elif idade > 12:
        ingresso = 30  # Ingresso de R$ 30,00 para pessoas com mais de 12 anos
        faixa_etaria = '13+'
    else:
        ingresso = 15  # Ingresso de R$ 15,00 para pessoas entre 4 e 12 anos
        faixa_etaria = '4-12'

    # Atualiza o relatório de custos por idade
    custos_por_idade[faixa_etaria] += ingresso

    # Atualiza o total de pessoas e o total em dinheiro arrecadado
    total_pessoas += 1
    total_dinheiro += ingresso

# Exibe o total de pessoas, o total arrecadado e o relatório de custos por idade
print(f'\nTotal de pessoas: {total_pessoas}')
print(f'Total arrecadado: R$ {total_dinheiro}\n')

print('Relatório de custos por idade:')
print(f'0-3 anos: R$ {custos_por_idade["0-3"]}')
print(f'4-12 anos: R$ {custos_por_idade["4-12"]}')
print(f'13+ anos: R$ {custos_por_idade["13+"]}')

print('Obrigado e tenha um ótimo filme')
