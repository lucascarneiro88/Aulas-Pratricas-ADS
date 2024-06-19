# condicional simples

# Função para imprimir o nome completo e o menu para o cliente
def imprimir_menu(nome_completo):
    print(f"Bem vindos a loja de Marmitas do {nome_completo}")
    print("Menu:")
    print("1 - Bife Acebolado (BA)")
    print("2 - Filé de Frango (FF)")
    print("Tamanhos disponíveis:")
    print("P - Pequeno")
    print("M - Médio")
    print("G - Grande")

# Função para calcular o preço com base no sabor e tamanho escolhidos
def calcular_preco(sabor, tamanho):
    # Tabela de preços conforme especificado
    if sabor == 'BA':
        if tamanho == 'P':
            return 16
        elif tamanho == 'M':
            return 18
        elif tamanho == 'G':
            return 22
        else:
            return None  # Tamanho inválido
    elif sabor == 'FF':
        if tamanho == 'P':
            return 15
        elif tamanho == 'M':
            return 17
        elif tamanho == 'G':
            return 21
        else:
            return None  # Tamanho inválido
    else:
        return None  # Sabor inválido

# Nome completo do programador
nome_completo = "ChatGPT da OpenAI"

# Impressão do nome completo e do menu inicial
imprimir_menu(nome_completo)

# Variável para acumular o valor total do pedido
total_pedido = 0

# Loop principal para processar múltiplos pedidos
while True:
    # Input do sabor da marmita
    sabor = input("Digite o sabor desejado (BA para Bife Acebolado ou FF para Filé de Frango): ").upper()
    
    # Verificação se o sabor é válido
    if sabor != 'BA' and sabor != 'FF':
        print("Sabor inválido. Tente novamente.")
        continue  # Reinicia o loop para pedir o sabor novamente
    
    # Input do tamanho da marmita
    tamanho = input("Digite o tamanho desejado (P, M ou G): ").upper()
    
    # Verificação se o tamanho é válido
    if tamanho not in ['P', 'M', 'G']:
        print("Tamanho inválido. Tente novamente.")
        continue  # Reinicia o loop para pedir o tamanho novamente
    
    # Cálculo do preço da marmita
    preco_marmita = calcular_preco(sabor, tamanho)
    
    # Verificação se o preço foi calculado com sucesso
    if preco_marmita is None:
        print("Erro no pedido. Tente novamente.")
        continue  # Reinicia o loop para pedir o pedido novamente
    
    # Acumula o preço no total do pedido
    total_pedido += preco_marmita
    
    # Pergunta se deseja pedir mais alguma coisa
    continuar = input("Deseja pedir mais alguma coisa? (s/n): ").lower()
    
    # Verificação se deseja continuar
    if continuar != 's':
        break  # Encerra o loop se a resposta não for 's'

# Exibe o total do pedido ao finalizar
print(f"Total do pedido: R$ {total_pedido:.2f}")
