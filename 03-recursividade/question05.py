def natural(n, y = 0):
	print(y)
	if(n > y):
		return natural(n, y+1)
	else:
		return ''

print(natural(5))
