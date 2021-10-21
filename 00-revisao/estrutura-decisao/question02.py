number1 = float(input('Insira o primeiro número: '))
number2 = float(input('Insira o segundo número: '))
number3 = float(input('Insira o terceiro número: '))

bigger = number1

if number2 > bigger:
	bigger = number2
if number3 > bigger:
	bigger = number3

smaller = number1

if number2 < smaller:
	smaller = number2
if number3 < smaller:
	smaller = number3

print(f'O maior número é o {bigger}')
print(f'O menor número é o {smaller}')
