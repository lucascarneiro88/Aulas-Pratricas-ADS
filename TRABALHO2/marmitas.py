# Exigência 1 de 8 
# OBS: # aspas duplas para delimitar a f-string porque há aspas simples dentro da string
print(f"{'-' * 10}  Bem vindos a loja de Marmitas do Lucas Carneiro {'-' * 10}")#exibe mensagem boas vindas
#exibe o menu cardapio com as opcoes
print('-' * 100)
print(f"{'-' * 20}     CARDÁPIO    {'-' * 20}")
print('-' * 100)
print(f"{'-' * 5} TAMANHO | Bife Acebolado (BA) | Filé de Frango (FF) |{'-' * 5}")
print(f"{'-' * 5}    P    |      R$ 16.00       |       R$ 15.00      |{'-' * 5}")
print(f"{'-' * 5}    M    |      R$ 18.00       |       R$ 17.00      |{'-' * 5}")
print(f"{'-' * 5}    G    |      R$ 22.00       |       R$ 21.00      |{'-' * 5}")
print('-' * 100)

# Inicia variavel total em 0 
total = 0

while True:  # inicia o loop
    # exigências 2 e 3 de 8
    sabor = input('Escolha o sabor (BA/FF):').upper()  # .upper para transformar em maiúscula e validar o que for digitado pelo input(Usuário)
    if sabor != 'BA' and sabor != 'FF':  # aqui verifica se o que for digitado for diferente dos sabores existentes ele exibe print sabor inválido
        print('Sabor inválido! Tente novamente.')
        continue  # retorna para o início do loop até ser digitado sabor válido

    tamanho = input('Escolha o tamanho (P/M/G):').upper()
    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
        print('Tamanho inválido! Tente novamente.')
        continue

    # Exigência 4 de 8
    if sabor == 'BA': #  se a escolha for  Bife Acebolado ele passa para o tamanho e se finalizar retorna preço
        tipoSabor = 'Bife Acebolado'
        if tamanho == 'P':
           custo = 16.00
        elif tamanho == 'M':
           custo = 18.00
        elif tamanho == 'G':
           custo = 22.00
    else: #  else ===== se não, o sabor for Frango Frito o escolhido ele  passa para o tamanho e se finalizar retorna preço
        sabor == 'FF'
        tipoSabor = 'Filé de Frango'
        if tamanho == 'P':
           custo = 15.00
        elif tamanho == 'M':
           custo = 17.00
        elif tamanho == 'G':
           custo = 21.00

    # Exigencia 5 de 8
    total +=custo # pega o preço do pedido e  soma o valor  a variavel atualizando-a 
    print(f'Pedido adicionado: {tipoSabor} tamanho {tamanho} por R$ {custo:.2f}')# print exibe o sabor,tamanho e o preço

    # Exigência 6 de 8
    # Pergunta se o usuario deseja pedir mais algum item do menu
    pedirNovamente = input('Deseja solicitar mais algum item? (S/N): ').upper() #Se digitar S(sim) continua se digitar N(não) encerra e passa para retornar o total
    if pedirNovamente != 'S': #se digitar algo diferente de S (sim) termina o programa retorna o total dos pedidos
        #Exigencia 7 de 8
        break

#Exigencia 8 de 8 ,comentários 
# Exibe oa soma do total de todos os pedidos 
print(f'Total a pagar: R$ {total:.2f}')# :.2f exibe 2 casas decimais após o ponto


















