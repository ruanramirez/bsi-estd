def evenOrOdd(number):
	if number % 2 == 0:
		return 'par'
	else:
		return 'ímpar'


number = int(input('Insira um número e verifique se é par ou ímpar: '))

print(f'O número {number} é {evenOrOdd(number)}')
