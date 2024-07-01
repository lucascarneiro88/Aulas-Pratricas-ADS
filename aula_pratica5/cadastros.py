cadastro = {'nome':[], 'sexo':[], 'ano':[]}

while True:
    encerrar = input('Deseja cadastrar um pessoa? [S/N]')
    if encerrar.upper() in 'N':
        break
    if encerrar.upper() not in 'S':
        print('Digite S para SIM ou N para Não')
        continue # volta para o inicio ate ser digitado o esperado

    nome = input('Digite o nome:')
    sexo = input('Digite o sexo:')
    ano = int(input('Digite o ano de nascimento:'))
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)

# Calcular total de cadastros
total_cadastros = len(cadastro['nome'])

# Calcular a média das idades
ano_atual = 2024  # pega o ano atual para calcular média
idades = [ano_atual - ano for ano in cadastro['ano']]
media_idade = round(sum(idades) / total_cadastros, 1)

# Lista de mulheres com menos de 30 anos
mulheres_menos_30 = [cadastro['nome'][i] 
        for i in range(total_cadastros) 
        if cadastro['sexo'][i] == 'F' and idades[i] < 30]
# Lista de homens com menos de 30 anos
homens_menos_30 = [cadastro['nome'][i] 
        for i in range(total_cadastros) 
        if cadastro['sexo'][i] == 'M' and idades[i] < 30]

# Lista com idades acima da média
acima_media = [cadastro['nome'][i] 
        for i in range(total_cadastros) 
        if idades[i] > media_idade]

print(f'Total de cadastros efetuados: {total_cadastros}')
print(f'Média das idades: {media_idade}')
print('Lista de mulheres com menos de 30 anos:', mulheres_menos_30)
print('Lista de homens com menos de 30 anos:', homens_menos_30)
print('Lista de pessoas com idade acima da média:', acima_media)
