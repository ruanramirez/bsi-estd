def modify():
	text = input('Insira um texto: ')
	if len(text) != 0:
		res = input('Palavra que você deseja alterar (y/n): ')

		if res == 'y':
			modifyText = input('Qual palavra? ')
			newText = input('Alterar para: ')

			return text.replace(modifyText, newText)

	return 'Inválido'

print(modify())
