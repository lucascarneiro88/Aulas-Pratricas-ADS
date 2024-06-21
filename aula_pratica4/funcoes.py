def fatorial(num):  # A variável num recebe o parâmetro
    fat = 1  # A variável fat só existe no corpo da função

    if num == 0:
        return fat

    # Esta parte só executa caso num for maior que 0
    for i in range(1, num + 1):
        fat *= i  # Mesma coisa que a escrita anterior que está comentada

    return fat  # Retorna o fatorial após o laço for terminar


x = int(input('Digite o valor para calcular a fatorial: '))
print(f'{x}! = {fatorial(x)}')  # O segundo x refere à variável num
