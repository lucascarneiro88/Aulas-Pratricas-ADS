def checagem_tipo(dado):
    match dado:
        case str(dado):
            print('string:', dado)
        case int(dado):
            print('inteiro:', dado)
        case float(dado):
            print('float:', dado)
        case _:
            print('Tipor desconhecido de dado!')

dados = ['python', 42, 3.14, 23, 'C']

for dado in dados:
    checagem_tipo(dado)
    