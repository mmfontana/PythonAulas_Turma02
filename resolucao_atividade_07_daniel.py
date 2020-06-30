import csv

lista_final = list()
lista_final_medias = list()
lista_final_nomes = list()

with open("medias_alunos.txt") as csv.file:
	csv_reader = csv.reader(csv.file)

	for linha in csv_reader:
		lista_final.append(linha)

for i in range(len(lista_final)):

	if not i == 0:
		linha = lista_final[i][0]
		linha = linha.split('\t')
		lista_final_nomes.append(linha[0])
		notas = linha[1:]

		media = 0
		for nota in notas:
			numero = float(nota)
			media += numero

		media_final = media/3
		lista_final_medias.append(media_final)

print(lista_final_medias)
print(lista_final_nomes)

with open("medias_alunos_out.txt", "w") as csv.file_out:
	csv_write = csv.writer(csv.file_out)
	

	for i in range(len(lista_final_medias)):
		lista_auxiliar = list()

		lista_auxiliar.append(lista_final_nomes[i])
		lista_auxiliar.append(lista_final_medias[i])

		csv_write.writerow(lista_auxiliar)
		





