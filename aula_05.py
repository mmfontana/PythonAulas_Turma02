# Metodos de lista


notas = [10, 8, 7, 4, 7, 8, 9]

# append
notas.append(6)

# extend

notas_extra = [4, 8, 9]

notas.extend(notas_extra)
notas.append('computador')
#notas.extend('computador')
#notas.extend(10)

# insert

nomes = ['Gabriel', 'Daniel', 'Marcos']

#nomes.insert(1, 'Maycon')

# nomes[0] = 'Maycon'

# Remove

# nomes.remove('Marcos')

# pop

# nomes.pop(0)

#nomes.clear()

# print(nomes.index('Daniel'))

notas = [10, 8, 7, 4, 7, 8, 9]

#notas.sort(reverse=True)

# Reverse
notas.reverse()

# print(notas)

# Copy

# notas_atualizadas = []
# notas_atualizadas = list()

notas_atualizadas = notas.copy()

#print(notas_atualizadas)

'''
nome = 'Fernando'

for letra in nome:
	print(letra)

lista = [2, 7, 9]

for numero in lista:
	print(numero)
'''
# idade = 35

peso = 45.8

#for numero in peso:
#	print(peso)


# Aula tuplas e dicionarios

primeira_tupla = (23.4, 18.5, 20.7)

# segunda_tupla = (18.5, 20.7, 23.4)

#primeira_tupla[0] = 78.5

peso_aluno = primeira_tupla[0]

#print(peso_aluno)

#print(type(primeira_tupla))


coordenada_estaca = (23.4, 54.2)

tupla_diferente = 2,4,5,7,10,12,15,18,19,19,19

#print(tupla_diferente)
#print(type(tupla_diferente))


#print(tupla_diferente.count(19))

#print(tupla_diferente.index(19))


#print(len(tupla_diferente))
#print(max(tupla_diferente))
#print(min(tupla_diferente))

nome = tuple('Livro')

tupla_vazia = tuple()

print(tupla_vazia)

print(nome)


magreza_moderada = (16, 17)



primeiro_dicionario = {'Maycon': {'idade': 45, 'altura': 2.2}, 
					   'Gabriel': {'idade': 45, 'altura': 2.2}, 
					   'Tiago': {'idade': 45, 'altura': 2.2}
					   }

print(primeiro_dicionario)
