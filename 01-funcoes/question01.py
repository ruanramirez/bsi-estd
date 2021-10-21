def factorial(number):
	fact = 1

	while number > 1:
		fact *= number
		number -= 1

	return fact

number = int(input('Insira um número inteiro e obtenha seu fatorial: '))

print(f'O fatorial de {number} ({number}!) é: {factorial(number)}')

