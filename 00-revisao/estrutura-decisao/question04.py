side1 = float(input('Insira o primeiro lado: '))
side2 = float(input('Insira o segundo lado: '))
side3 = float(input('Insira o terceiro lado: '))

if (side1 + side2 < side3) or (side1 + side3 < side2) or (side2 + side3 < side1):
	print('Nao é um triângulo')
elif (side1 == side2) and (side1 == side3):
	print('Triângulo equilátero')
elif (side1 == side2) or (side1 == side3) or (side2 == side3):
	print('Triângulo isósceles')
else:
	print('Triângulo escaleno')
