def reverse_string(string):
	if len(string) != 0:
		return string[::-1]

	return False

def pali(string):
	if reverse_string(string):
		reverse = reverse_string(string)

		if string != reverse:
			return f'A palavra "{string}" não é palíndroma'

		return f'A palavra "{string}" é palíndroma'

	return 'Inválido'

print(pali('ruan'))
print(pali(''))
print(pali('ana'))
