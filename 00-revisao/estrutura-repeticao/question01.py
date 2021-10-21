number = int(input('Insira uma nota entre 0 e 10: '))

if number >= 0 and number <= 10:
	print(f'O numero {number} obedece as restrições.')

while number < 0 or number > 10:
	print(f'O numero {number} não obedece as restrições. Tente novamente!')
	number = int(input('Insira uma nota entre 0 e 10: '))

	if number >= 0 and number <= 10:
		print(f'O numero {number} obedece as restrições.')
