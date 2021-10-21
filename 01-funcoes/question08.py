def hipotenusa(co, ca):
	return ((co ** 2) + (ca ** 2)) ** (1/2)

co = float(input('Insira o cateto oposto: '))
ca = float(input('Insira o cateto adjacente: '))

print(f'A hipotenusa é: {round(hipotenusa(co, ca), 2)}')
