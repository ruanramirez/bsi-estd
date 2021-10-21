number = int(input('Informe um ano e verifique se é bissexto ou não: '))

if (number % 4 == 0 and number % 100 != 0) or (number % 400 == 0):
	print(f'O ano {number} é bissexto.')
else:
	print(f'O ano {number} não é bissexto.')
