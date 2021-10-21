i = 1
isSum = 0

while i <= 5:
	number = float(input('Insira um número: '))
	isSum += number

	i += 1

average = isSum / 5

print(f'A média é: {average}')
