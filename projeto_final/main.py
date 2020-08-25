from raspador import Raspador

# Objecto para raspagem
amazon_raspador = Raspador(numero_paginas=2)
# Soup das paginas
soup_paginas = amazon_raspador.raspa_pagina()
# Raspagem dos dados
dados = amazon_raspador.raspa_dados(soup_paginas)
