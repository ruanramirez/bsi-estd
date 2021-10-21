day = int(input('Insira o dia (dd): ') )
month = int(input('Insira o mês (mm): ') )
year = int(input('Insira o ano (aaaa): ') )

valid = False

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
	if day <= 31:
		valid = True

elif month == 4 or month == 6 or month == 9 or month == 11:
	if day <= 30:
		valid = True

elif month == 2:
	if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
		if day <= 29:
			valid = True
	elif day <= 28:
			valid = True

if day <= 0 or month <= 0 or year <= 0:
	valid = False

if(valid):
	print(f'{day}/{month}/{year} é uma data válida')

else:
	print(f'{day}/{month}/{year} é uma data inválida')
