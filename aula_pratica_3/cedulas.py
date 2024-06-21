valor = int(input('Digite o valor em R$:'))

while True:
    if valor >= 100:
        contador100 = valor // 100  # // para dividir valor exato inteiro
        valor = valor - contador100 * 100
        print(f'Cédulas de 100:{contador100}')

        #  condição para fazer o break quando encerrar
        if not valor:
           break

        if valor >= 50:
          contador50 = valor // 50  # // para dividir valor exato inteiro
          valor = valor - contador50 * 50
          print(f'Cédulas de 50:{contador50}')

           #  condição para fazer o break quando encerrar
        if not valor:
           break

        if valor >= 20:
          contador20 = valor // 20  # // para dividir valor exato inteiro
          valor = valor - contador20 * 20
          print(f'Cédulas de 20:{contador20}')

             #  condição para fazer o break quando encerrar
        if not valor:
           break

        if valor >= 10:
          contador10 = valor // 10  # // para dividir valor exato inteiro
          valor = valor - contador10 * 10
          print(f'Cédulas de 10:{contador10}')

             #  condição para fazer o break quando encerrar
        if not valor:
           break

        if valor >= 5:
           contador5 = valor // 5
           valor = valor - contador5 * 5
           print(f'Cédulas de 5: {contador5}')

              #  condição para fazer o break quando encerrar
        if not valor:
           break

        if valor:
           contador1 = valor
           print(f'Cédulas de 1: {contador1}')
           break

