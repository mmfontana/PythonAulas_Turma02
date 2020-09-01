import pytest
from raspador import Raspador

def test_classe_principal():
	raspador = Raspador(numero_paginas=2)
	assert type(raspador) == type(Raspador(numero_paginas=-999))

def test_numero_paginas():
	raspador = Raspador(numero_paginas=2)
	soup_paginas = raspador.raspa_pagina()
	dados = raspador.raspa_dados(soup_paginas)
	assert type(dados) == type(list())
	assert raspador.numero_paginas == len(soup_paginas)

def test_listas_finais():
	raspador = Raspador(numero_paginas=2)
	soup_paginas = raspador.raspa_pagina()
	dados = raspador.raspa_dados(soup_paginas)
	dados_df = raspador.cria_dicionario(dados)
	dados_df = raspador.tratamento_string(dados_df)

	assert	len(dados_df['nomes']) == 100
	assert	len(dados_df['autores']) == 100		
	assert	len(dados_df['colocacoes']) == 100
	assert	len(dados_df['numero_avaliacoes']) == 100
	assert	len(dados_df['precos']) == 100


