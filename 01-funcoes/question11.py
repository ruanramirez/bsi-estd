def sumNumbers(number):
	listNum = []

	for num in range(1, number + 1):
		listNum.append(num)

	return sum(listNum)

print(sumNumbers(7))
