def soma(x=0, y=0, z=0):

    #Observação: no pycharm digitando 3 aspas simples ele ja reconhece os parametros
    # e autocompleta praticamente a docstring
    """
    Explicação do funcionamento da função.
    Calcula a soma de três números.

    
    :paran   x (int, optional): O primeiro número. O padrão é 0.
    :paran   y (int, optional): O segundo número. O padrão é 0.
    :paran  z (int, optional): O terceiro número. O padrão é 0.

    Return:
        int: A soma dos três números.
    """
    return x + y + z

print(soma(3, 2))  # Imprime 5
help(soma)  # Exibe a documentação da função soma
