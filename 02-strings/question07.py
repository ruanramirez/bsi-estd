def login(string):
	if len(string) != 0:
		string = string.lower()
		string = string.split(' ')
		string = [x[0] for x in string]

		return ''.join(string)

	return 'Inválido'

print(login('Ruan Ramírez Limeira Soares'))
