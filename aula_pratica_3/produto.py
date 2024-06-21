#exercicios
# mostrar 4 produtos
print('LANCHONETE')
print('1 - Coxinha R$ 5,00')
print('2 - empada R$ 5,00')
print('3 - pastel R$ 6,00')
print('4 - café R$ 3,00')
print('5 - SAIR')

total = 0
# Menu infinito com as opções ate o breack
while True:
    operador = int(input('Qual item gostaria de comoprar?'))
   

    if (operador == 1):
         quantidade = int(input('Quantas unidades quer?'))
         total = total + quantidade * 5.00
    elif (operador == 2):
         quantidade = int(input('Quantas unidades quer?'))
         total = total + quantidade * 5.00
    elif (operador == 3):
         quantidade = int(input('Quantas unidades quer?'))
         total = total + quantidade * 6.00
    elif (operador == 4):
         quantidade = int(input('Quantas unidades quer?'))
         total = total + quantidade * 3.00
    elif (operador == 5):
        break
    else:
        print('Produto invalido, selecione outro produto.')

print(f'\nTotal a pagar é de R$: {total}.')
   
