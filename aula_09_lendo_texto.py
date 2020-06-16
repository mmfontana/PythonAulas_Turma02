import csv

lista_final = list()

with open("medias_alunos.txt") as csv_file:

	csv_reader = csv.reader(csv_file)		

	for linha in csv_reader:
		
		lista_final.append(linha)

for i in range(len(lista_final)):

	if not i == 0:

		linha = lista_final[i][0]
		linha = linha.split('\t')
		notas = linha[1:]

		media = 0
		for nota in notas:

			numero = float(nota)
			media += numero

		media_final = media/3
		print(media_final)

# 