def bigger(numberA, numberB):
	if numberA > numberB:
		return numberA
	elif numberB > numberA:
		return numberB
	else:
		return f'{numberA} = {numberB}'

print(f'A: 2, B: 1 | Maior: {bigger(2, 1)}')
print(f'A: 1, B: 2 | Maior: {bigger(1, 2)}')
print(f'A: 2, B: 2 | Igualdade: {bigger(2, 2)}')
