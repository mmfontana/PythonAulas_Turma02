# Exercicio 1 
'''
notas = [8, 7, 5, 4, 3, 2, 1, 10, 5]

soma = 0

for nota in notas:
	soma += nota

print(soma)
'''

# Exercicio 2

notas = [7, 7, 5, 2, 8, 10, 8, 7, 3, 3, 10, 2, 5, 10, 5]

lista_unicos = list()

for nota in notas:
	if nota not in lista_unicos:
		lista_unicos.append(nota)

print(lista_unicos)
