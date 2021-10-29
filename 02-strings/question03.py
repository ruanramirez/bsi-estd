def last(string):
	if len(string) != 0:
		string = string.split(' ')
		return string[-1]

	return 'Inválido'


print(last('Ruan Ramírez'))
