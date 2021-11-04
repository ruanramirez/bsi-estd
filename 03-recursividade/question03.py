def countString(string, letter):
	if len(string) == 0:
		return 0
	else:
		count = 0
		for s in string:
			if s == letter:
				count += 1
