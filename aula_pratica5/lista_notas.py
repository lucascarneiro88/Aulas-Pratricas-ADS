#Para saber quantos alunos tiraram nota 7

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
print(notas.count(7))

#para altera ultimo numero da lista
notas [-1] = 4 
print(notas)

#encontar o maior numero na lista
print(max(notas))

#ordenar listas de notas
notas.sort()
print(notas)

#media das notas
print(sum(notas) / len(notas))