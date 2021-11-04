def invertString(string):
	if len(string) > 0:
		return invertString(string[1:]) + string[0]

	return ''

print(invertString('Python'))
