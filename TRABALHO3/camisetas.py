# Exigencia 1 de 7
print('Bem vindos a Fábrica de Camisetas do Lucas Carneiro')

# Exigencia 2 de 7
# Função para escolher modelo camiseta
def escolhaDeModelo():
    # Inicia o loop de escolha até ser digitada uma opção válida 
    while True: # Repete a pergunta do item B.a se digitar uma opção diferente de: MCS/MLS/MCE/MLE;
        # MCS = Manga Curta Simples/ MLS = Manga Longa Simples/ MCE = Manga Curta Com Estampa/ MLE = Manga Longa Com Estampa
        # (input) Pergunta o modelo desejado
        modeloDeCamiseta = input('Escolha o modelo (MCS/MLS/MCE/MLE): ').upper() # .upper p/ transformar tudo em maiúscula para não gerar erro referente ao que for digitado

        if modeloDeCamiseta == 'MCS':
            return 'Manga Curta Simples', 1.80 # Retorna o valor do modelo com base na escolha do usuário/valor unitário é de um real e oitenta centavos
        elif modeloDeCamiseta == 'MLS':
            return 'Manga Longa Simples', 2.10 # o valor unitário é de dois reais e dez centavos
        elif modeloDeCamiseta == 'MCE':
            return 'Manga Curta Com Estampa', 2.90 # o valor unitário é de dois reais e noventa centavos
        elif modeloDeCamiseta == 'MLE':
            return 'Manga Longa Com Estampa', 3.20 # o valor unitário é de três reais e vinte centavos
        else:
            print('Opção inválida! Tente novamente.') # print se a escolha não for uma opção

# Função para escolher a quantidade de camisetas
# Exigencia 3 de 7
def quantidadeDeCamisetas():
    while True:
        # Exigencia 5 de 7: uso do try / except
        try:
            camisetas = int(input('Digite a quantidade de camisetas: '))
            
            if camisetas > 20000:
                print('Não aceitamos pedidos nessa quantidade. Tente novamente.')
            else:
                if camisetas < 20:
                    desconto = 0.0 # Se número de camisetas for menor que 20 não há desconto na venda
                elif 20 <= camisetas < 200:
                    desconto = 0.05 # Se número de camisetas for igual ou maior que 20 e menor que 200, o desconto será de 5%
                elif 200 <= camisetas < 2000:
                    desconto = 0.07 # Se número de camisetas for igual ou maior que 200 e menor que 2000, o desconto será de 7%
                elif 2000 <= camisetas <= 20000:
                    desconto = 0.12 # Se número de camisetas for igual ou maior que 2000 e menor ou igual a 20000, o desconto será de 12%
                return camisetas, desconto
                
        except ValueError:
            print('Valor inválido, por favor digite um número válido.')

# Função para escolha do tipo de frete
# Exigencia 4 de 7
def frete():
    while True: # Repete a pergunta item D.a se digitar uma opção diferente de: 1/2/0
        opcaoFrete = input('Escolha o frete (1 - Transportadora / 2 - Sedex / 0 - Retirar na Fábrica): ') # Pergunta pelo serviço adicional de frete
        if opcaoFrete == '1':
            return 'Transportadora', 100.00 # Para o adicional de frete por transportadora (1) é cobrado um valor extra de 100 reais
        elif opcaoFrete == '2':
            return 'Sedex', 200.00 # Para o adicional de frete por Sedex (2) é cobrado um valor extra de 200 reais
        elif opcaoFrete == '0':
            return 'Retirar na Fábrica', 0.00 # Para o adicional de retirar o pedido na fábrica (0) é cobrado um valor extra de 0 reais
        else:
            print('Opção inválida. Tente novamente.')

# Programa principal (main)
# Deve-se implementar o total a pagar no código principal (main), ou seja, não pode estar dentro de função, conforme o enunciado
# Exigencia 5 de 7
if __name__ == '__main__': # padrão python para nomear programa principal
    modelo, valorUnidade = escolhaDeModelo() # Solicita o modelo e obtem o valor da unidade

    quantidadeCamisetas, desconto = quantidadeDeCamisetas() # Solicita a quantidade de camisetas p/ obter o desconto

    valorTotalCamisetas = quantidadeCamisetas * valorUnidade * (1 - desconto) # Calculo do valor total de camisetas com o desconto
    
    freteEscolhido, valorFrete = frete() # Solicita a opção do frete p/ obter o valor a ser calculado

    totalPagar = valorTotalCamisetas + valorFrete # Calcula o valor total a ser pago incluindo o frete

    # Exibição detalhada dos cálculos e valores em um único print
    print(f'Total: R$ {totalPagar:.2f} (modelo: {valorUnidade * quantidadeCamisetas:.2f} (com desconto: {valorTotalCamisetas:.2f}) + frete: {valorFrete:.2f})')
