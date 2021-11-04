def natural(n, y = 0):
	print(n)
	if(n > y):
		return natural(n -1, y)
	else:
		return ''

print(natural(5))
