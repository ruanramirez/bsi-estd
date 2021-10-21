number1 = float(input('Insira a primeira nota: '))
number2 = float(input('Insira a segunda nota: '))

average = (number1 + number2) / 2

if average >= 7 and average < 10:
	print('Aprovado')
elif average >= 10:
	print('Aprovado com Distinção')
else:
	print('Reprovado')
