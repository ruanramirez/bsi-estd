countryA = 80000
rateA = 0.03

countryB = 200000
rateB = 0.015

age = 0

while countryA <= countryB:
	countryA += countryA * rateA
	countryB += countryB * rateB
	age += 1

print(f'O país A ultrapassa ou iguala ao país B em {age} anos')
