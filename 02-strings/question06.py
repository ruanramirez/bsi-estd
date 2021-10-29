def space(string):
	if len(string) != 0:
		string = list(string.upper())

		return ' '.join(string)

	return 'Inválido'

print(space('Ruan'))
print(space('Ruan Ramírez'))
print(space('ruan'))

