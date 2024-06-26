print('Escolha o produto:')
print('1 - Maçã')
print('2 - Laranja')
print('3 - Banana')

produto = int(input('Qual a sua escolha?'))
quantidade = int(input('Quantas unidades do produto?'))

match (produto):
    case 1:
        pagar = quantidade * 2.3
        print(f'Você comprou {quantidade} maçãs. Total a pagar : {pagar}')
    case 2:
        pagar = quantidade * 3.6
        print(f'Você comprou {quantidade} laranjas. Total a pagar: {pagar}')
    case 3:
        pagar = quantidade * 1.85
        print(f'Você comprou {quantidade} bananas. Total a pagar {pagar}')
    case _:
        print('Produto sem estoque, ou inexistente!')



