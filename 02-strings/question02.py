def countString(string):
	if len(string) != 0:
		sup = string.split(' ')
		count = len(sup)
		for x in sup:
			if x == '':
				return count - 1
		return count

	return 'Inválido'

print(countString('Ruan Ramirez'))
print(countString(' Ruan Ramirez'))

