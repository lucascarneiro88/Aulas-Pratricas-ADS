def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x 


def fatorial(num):  # A variável num recebe o parâmetro
    fat = 1  # A variável fat só existe no corpo da função
    """
    Função que calcula o fatorial de um número inteiro.

    O fatorial de um número inteiro não negativo n é o produto de todos os inteiros positivos menores ou iguais a n.
    É representado por n! e definido como n! = 1 * 2 * 3 * ... * n. Por convenção, 0! é definido como 1.

    Args:
        num (int): O número inteiro cujo fatorial será calculado. Deve ser um inteiro não negativo.

    Returns:
        int: O fatorial do número fornecido. Se num for 0, retorna 1.

    Raises:
        ValueError: Se o argumento fornecido não for um número inteiro não negativo.
    """
    if num == 0:
        return fat

    # Esta parte só executa caso num for maior que 0
    for i in range(1, num + 1, 1):
        fat *= i  # Mesma coisa que a escrita anterior que está comentada

    return fat  # Retorna o fatorial após o laço for terminar


# x = int(input('Digite o valor para calcular a fatorial: '))
x = valida_int('Digite um valor para calcular a fatorial:', 0 , 99999)
print(f'{x}! = {fatorial(x)}')  # O segundo x refere à variável num
