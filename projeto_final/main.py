from raspador import Raspador

# Objecto para raspagem
amazon_raspador = Raspador(numero_paginas=2)
# Soup das paginas
soup_paginas = amazon_raspador.raspa_pagina()
# Raspagem dos dados
dados = amazon_raspador.raspa_dados(soup_paginas)
# Criacao dicionario
dados_df = amazon_raspador.cria_dicionario(dados)
# Tratamento strings 
dados_df = amazon_raspador.tratamento_string(dados_df)
# Para df
df = amazon_raspador.para_pandas(dados_df,'amazon.csv')


print(df)