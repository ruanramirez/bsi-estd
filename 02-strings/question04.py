def transform(string):
	if len(string) != 0:
		string = string.split(' ')
		return f'{string[-1]}/{string[0]}'

	return 'Inválido'

print(transform('Ruan Ramírez Limeira Soares'))
