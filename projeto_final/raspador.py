import requests
from bs4 import BeautifulSoup
import pandas as pd

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
		numeros_avaliacoes = list()
		precos = list()
		# Criar parte do raspador para notas usuarios


		for i in range(len(soup_paginas)):

			for d in soup_paginas[i].findAll('div', attrs={'class': 'a-section a-spacing-none aok-relative'}):

				# Nome do livro
				nome = d.find('span', attrs={'class': 'zg-text-center-align'})
				nome_in = nome.find_all('img', alt=True)
				# Autor do livro
				autor = d.find('span', attrs={'class': 'a-size-small a-color-base'})
				# Colocacao do livro
				colocacao = d.find('span', attrs={'class': 'zg-badge-text'})
				# Numero de avaliacoes
				numero_avaliacoes = d.find('a', attrs={'class': 'a-size-small a-link-normal'})
				# Preco do livro
				preco = d.find('span', attrs={'class': 'p13n-sc-price'})

				if nome_in is not None:
					nomes.append(nome_in[0]['alt'])
				else:
					nomes.append('nan')
				if autor is not None:
					autores.append(autor.text)
				else:
					autores.append('nan')
				if colocacao is not None:
					colocacoes.append(colocacao.text)
				else:
					colocacoes.append('nan')
				if numero_avaliacoes is not None:
					numeros_avaliacoes.append(numero_avaliacoes.text)
				else:
					numeros_avaliacoes.append('nan')
				if preco is not None:
					precos.append(preco.text)
				else:
					precos.append('nan')

		dados = [nomes, autores, colocacoes, numeros_avaliacoes, precos]	

		return dados

	def cria_dicionario(self, dados):

		dados_df = dict()

		dados_df['nomes'] = dados[0]
		dados_df['autores'] = dados[1]		
		dados_df['colocacoes'] = dados[2]
		dados_df['numero_avaliacoes'] = dados[3]
		dados_df['precos'] = dados[4]

		return dados_df

	def tratamento_string(self, dados_df):

		for i in range(len(dados_df['colocacoes'])):
			try:
				dados_df['colocacoes'][i] = float(dados_df['colocacoes'][i].split('#')[1])
			except:
				pass

		for i in range(len(dados_df['numero_avaliacoes'])):
			try:
				dados_df['numero_avaliacoes'][i] = float(dados_df['numero_avaliacoes'][i].replace('.',''))
			except:
				pass

		for i in range(len(dados_df['precos'])):
			try:
				dados_df['precos'][i] = dados_df['precos'][i].split('R$')[1]
				dados_df['precos'][i] = float(dados_df['precos'][i].replace(',','.'))
			except:
				pass

		return dados_df

	def para_pandas(self, dados_df, arquivo):

		df = pd.DataFrame(dados_df)
		df.to_csv(arquivo)

		return df
