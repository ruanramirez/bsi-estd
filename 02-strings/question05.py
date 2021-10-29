def transform(string):
	if len(string) != 0:
		string = string.split(' ')
		init = [x[0] for x in string]
		init = init[1:]
		init = '. '.join(init)
		return f'{string[-1]}, {init}.'

	return 'Inválido'

print(transform('Ruan Ramírez Limeira Soares'))
