print('Bem-Vindos a loja do Lucas Carneiro')# print nome app 

#Exigência 1 de 6 (inputs)
valorPedido = float(input('Digite o valor do pedido:R$'))
quantidadeParcelas = int(input('Em quantas parcelas deseja fazer?'))

#Exigência 2 de 6
#Exigencia 5 de 6 (if, elif e else)
#Exigencia 6 de 6 comentar código
if quantidadeParcelas < 4:#Juros relaticvo a quantidade de parcelas(estrutura condicional)
    juros = 0.00 # 0 % de juros 
elif quantidadeParcelas >= 4 and quantidadeParcelas < 6:
    juros = 0.04 # 4% de juuros
elif quantidadeParcelas >= 6 and quantidadeParcelas < 9:
    juros = 0.08 # 8% de juros
elif quantidadeParcelas >= 9 and  quantidadeParcelas < 13:
    juros = 0.16 # 16% de juros
else:
    juros = 0.32 # 32% de juros

#exigencias 4 de 6
#Calculo valor parcela
valorParcela = valorPedido * (1 + juros)/ quantidadeParcelas

#Calculo valor total parcelado
valorTotalParcelado = valorParcela * quantidadeParcelas

#exibe a quantidade de parcelas e os juros aplicados ao valor
if quantidadeParcelas >= 4:
    print(f"Você escolheu {quantidadeParcelas} parcelas e o valor com juros parcelados neste caso é: R${valorParcela:.2f}")# :.2f para exibir 2 casas decimais
    print(f"O valor total parcelado é: R${valorTotalParcelado:.2f}") 

# exibira o valor referente a parcela mnor que 4 que o juros é 0%
else:
    print(f"O valor total da parcela sem juros é: R${valorTotalParcelado:.2f}")