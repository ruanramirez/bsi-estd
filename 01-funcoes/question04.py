def compare(numberA, numberB):
	if numberA > numberB:
		return 1
	elif numberA == numberB:
		return 0
	elif numberA < numberB:
		return -1

print(f'A > B: {compare(3, 2)}')
print(f'A = B: {compare(3, 3)}')
print(f'A < B: {compare(2, 3)}')
