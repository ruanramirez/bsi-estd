def dayByDayWeek(dayNumber):
	week = [
		'1 - Domingo',
		'2 - Segunda-feira',
		'3 - Terça-feira',
		'4 - Quarta-feira',
		'5 - Quinta-feira',
		'6 - Sexta-feira',
		'7 - Sábado'
	]

	if dayNumber >= 1 and dayNumber <= 7:
		for number in week:
			number = dayNumber - 1
			return week[number]
	else:
		return 'Inválido'


dayNumber = int(input('Insira um número entre 1 e 7 e obtenha o dia da semana equivalente: '))

print(f'Você digitou: {dayByDayWeek(dayNumber)}')
