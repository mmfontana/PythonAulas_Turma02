import requests
from bs4 import BeautifulSoup

class Raspador():

	def __init__(self, numero_paginas):

		self.numero_paginas = numero_paginas

	def raspa_pagina(self):

		soup_paginas = list()

		for i in range(1,self.numero_paginas+1):

			request = requests.get('https://www.amazon.com.br/gp/bestsellers/books/ref=zg_bs_pg_1?ie=UTF8&pg={}'.format(i))
			conteudo = request.content
			soup = BeautifulSoup(conteudo, features="html.parser")
			soup_paginas.append(soup)

		return soup_paginas

	def raspa_dados(self, soup_paginas):

		nomes = list()
		autores = list()
		colocacoes = list()
		notas_usuarios = list()
		precos = list()


		for i in range(len(soup_paginas)):

			for d in soup_paginas[i].findAll('div', attrs={'class': 'a-section a-spacing-none aok-relative'}):

				# Nome do livro
				nome = d.find('span', attrs={'class': 'zg-text-center-align'})
				nome_in = nome.find_all('img', alt=True)
				# Autor do livro
				autor = d.find('span', attrs={'class': 'a-size-small a-color-base'})
				# Colocacao do livro
				colocacao = d.find('span', attrs={'class': 'zg-badge-text'})
				# Nota dos usuarios
				nota_usuarios = d.find('a', attrs={'class': 'a-size-small a-link-normal'})
				# Preco do livro
				preco = d.find('span', attrs={'class': 'p13n-sc-price'})

				
				# Exercicio: colocar estrutura else para cada if. Passando um string 'nan' para a lista.
				if nome_in is not None:
					nomes.append(nome_in[0]['alt'])
				if autor is not None:
					autores.append(autor.text)
				if colocacao is not None:
					colocacoes.append(colocacao.text)
				if nota_usuarios is not None:
					notas_usuarios.append(nota_usuarios.text)
				if preco is not None:
					precos.append(preco.text)

		dados = [nomes, autores, colocacoes, notas_usuarios, precos]	

		return dados


		# Exercicio: criar metodo para transformar a lista de dados num dicionario estruturado.
		# def ...
		# Formato dicionario: dict = {'nomes': nomes, 'autores': autores}

