# if (2 + 2 <= 4):
#     print("verdadeiro")

# if (7 // 3 == 1+1):
#     print("verdadeiro!")

# if (3**2 + 4**2 == 25):
#     print("Verdadeiro!")


# if (1387 % 19 == 0):
#     print('Verdadeiro!')

# if (31 % 2 == 0):
#     print('Verdadeiro!')
# else:
#     print('numero não é par')


# if (min(34, 29, 31 < 30)):
#     print('Verdadeiro!')


# ***********************************************CONDICIONAL SIMPLES **********************

# idade = 65
# if ('idade >  60'):
#     print('voce tem direitos ao beneficios')


# dano = 15
# escudo = 0

# if(dano > 10 and escudo == 0):
#     print('voce esta morto')

# norte = False
# sul = False
# leste = False
# oeste = True

# if (norte == True or sul == True or leste == True or oeste == True):
#    print('voce escapou')


# ***********************************************CONDICIONAL COMPOSTA **********************
# ano = 3
# if (ano % 4 == 0):
#     print('Pode ser um ano bissexto')
# else:
#     print('Definitivamente não é um ano bissexto')

# cima = True
# baixo = True

# if (cima == True and baixo == True):
#     print('Decida-se')
# else:
#     print('Você escolheu um caminho')    

# _______************************** TRIANGULO**********************

# Solicitando os lados do triângulo
# lado1 = int(input('Digite o primeiro lado: '))
# lado2 = int(input('Digite o segundo lado: '))
# lado3 = int(input('Digite o terceiro lado: '))

# # Verificando se os valores podem formar um triângulo válido
# if (lado1 > 0 and lado2 > 0 and lado3 > 0 and
#     lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1):
#     # Classificando o triângulo
#     if lado1 == lado2 == lado3:
#         print('Este é um triângulo equilátero de 3 lados iguais')
#     elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
#         print('Este é um triângulo escaleno de 3 lados diferentes')
#     else:
#         print('Este é um triângulo isósceles de 2 lados iguais')
# else:
#     print('Os valores fornecidos não formam um triângulo válido')

# # Condição adicional para verificar se algum lado é zero (não necessário pois já está incluído na verificação inicial)
# if lado1 == 0 or lado2 == 0 or lado3 == 0:
#     print('Digite um número positivo diferente de zero')

# francisca = True
# megan = True

# if(francisca == megan):
#     print('irmazinhas')
# else:
#     print("vão se espancar")    

# ****************************************VALORES*******************
# valor1 = ()
# Valor2 = ()

valor1 = int(input('Digite o primeiro valor:'))
valor2 = int(input('Digite o segundo valor:'))
print('Adição +')
print('subtração -')
print('Multiplicação *')
print('Divisão /')


operacao = input('Escolha a operação que deseja fazer :')



if (operacao == '+'):
    resultado= valor1 + valor2
    print(f'A soma é:{resultado}')

elif (operacao == '-'):
    resultado = valor1 - valor2
    print(f'A subtração é: {resultado}') 

elif (operacao == '*'):
    resultado = valor1 * valor2
    print(f'O resultado da multiplicação é: {resultado}')

elif (operacao == '/'):
     if valor2 != 0:
        resultado = valor1 // valor2        
        print(f'O resultado da divisão é: {resultado}')
     else:
        print('Erro: não é permitido fazer a operação de divisão por 0')

else:
    print('Operação inválida. Escolha entre: soma, subtracao, multiplicacao, divisao.')

    
