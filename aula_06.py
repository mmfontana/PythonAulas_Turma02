# Dicionarios

# Dicionarios aninhados

d = {'Daniel':{'idade': 85, 'altura': 1.9, 'peso': 80}, 'Maycon':{'idade': 90, 'altura': 1.7, 'peso': 90}}

'''
peso_daniel = d['Daniel']['peso']

d['Marcos'] = {'idade': 70, 'altura': 1.6, 'peso': 70}

print(peso_daniel)

d['Maycon']['peso'] = 95

print(d)


# Dicionario misto

d_1 = dict()

d_1['valores']  = [37.6, 74.2, 89.2]

d_1['nome'] = 'Maycon'

print(d_1)
'''

# Dicionario de coordenadas

pontos_turisticos = {(20.5, 42.8): 'Catedral', (20.7, 42.9): 'Praça XV'}

#print(pontos_turisticos)

# pontos_turisticos = {[20.5, 42.8]: 'Catedral', [20.7, 42.9]: 'Praça XV'} --> nao funciona, listas sao mutaveis


# Metodos para dicionario

pontos_turisticos.clear()

#print(pontos_turisticos)

items = list()
items = d.items()

#print(items)

lista_chaves = []
lista_chaves = d.keys()

print(lista_chaves)

lista_valores = []
lista_valores = d.values()

print(lista_valores)


d.pop()

print(d)



