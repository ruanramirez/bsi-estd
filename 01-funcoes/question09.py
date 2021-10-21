def isLeap(year):
	if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
		return True
	else:
		return False

year = int(input('Insira um ano e verifique se é bissexto ou não: '))

if year <= 0 :
	print(f'O ano {year} é inválido.')
elif isLeap(year):
	print(f'O ano {year} é bissexto.')
else:
	print(f'O ano {year} não é bissexto.')
