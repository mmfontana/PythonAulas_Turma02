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

