def isEven(number):
	if number % 2 == 0:
		return True
	else:
		return False

number = int(input('Insira um número inteiro e verifique se é par ou ímpar: '))

support = isEven(number)

if support == False:
	print(f'O número {number} é impar.')
else:
	print(f'O número {number} é par.')

