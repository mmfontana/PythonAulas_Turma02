import requests
from bs4 import BeautifulSoup

class Raspador():

	def __init__(self):

		pass

	def RaspaPagina(self):

		# for para trocar a url de pagina, fazendo o request na pagina 1 e 2  

		request = requests.get('https://www.amazon.com.br/gp/bestsellers/books/ref=zg_bs_pg_1?ie=UTF8&pg=1')
		conteudo = request.content

		return conteudo