# Metodos para string

nome = 'Gabriel'

#nome = nome.lower()

nome = nome.upper()

nome_aluno = 'Marcos'

nome_aluno_curto = nome_aluno.strip()

#print(len(nome_aluno))
#print(len(nome_aluno_curto))
#print(nome_aluno)

verificacao = nome_aluno.isalpha()

numero = '1001'
verificacao_numero = numero.isdigit()
#int(numero)
#print(verificacao_numero)


branco = '\t'
verificacao_branco = branco.isspace()
#print(verificacao_branco)
#print(type(branco))

nome_longo = 'maycon machado fontana'
primeiro_nome = 'maycon machado'

teste_inicio = nome_longo.startswith(primeiro_nome)

#print(teste_inicio)
ultimo_nome = nome_longo
teste_final = nome_longo.endswith(ultimo_nome)
#print(teste_final)


indice = nome_longo.find('yo')

#print(indice)

nome_curto = nome_longo.replace('machado', '')
nome_curto = nome_curto.replace('  ', ' ')
#print(nome_curto)


nome_in = 'Daniel Alencastro Souza Matos Machado'
nomes = nome_in.split(' ')
#print(nomes)

nome_daniel = nomes[0] + ' ' + nomes[-1]
#print(nome_daniel)


primeiro_nome = 'Daniel'
primeiro_sobrenome = 'Alencastro'
segundo_sobrenome = 'Souza'

#nome_completo = primeiro_nome.join('Alencastro')

#print(nome_completo)

nome_com_virgulas = 'CASA'.join([primeiro_nome, primeiro_sobrenome, segundo_sobrenome])

print(nome_com_virgulas)
print(type(nome_com_virgulas))


