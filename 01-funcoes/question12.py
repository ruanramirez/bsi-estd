def isPrime(number):
	count = 0
	for num in range(1, number + 1):
		if number % num == 0:
			count += 1

	if count == 2:
		return 'É primo'
	else:
		return 'Não é primo'

print(isPrime(1))
print(isPrime(2))
print(isPrime(3))
print(isPrime(9))
print(isPrime(13))
