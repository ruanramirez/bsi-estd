def doubleFact(n):
	if(n == 1):
		return 1

	if(n % 2 == 0):
		return 0

	return n * doubleFact(n - 2)

print(doubleFact(5))
