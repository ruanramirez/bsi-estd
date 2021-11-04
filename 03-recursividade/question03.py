def countString(string, letter):
	if len(string) == 0:
		return 0
	else:
		if string[0] == letter:
			return countString(string[1:], letter) + 1
		else:
			return countString(string[1:], letter)

print(countString('recursividade', 'r'))
