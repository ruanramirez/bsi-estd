def isDateValid(day, month, year):
	if day <= 0 or month <= 0 or year <= 0:
		return False

	if day > 0 and day <= 31:
		if month > 0 and month <= 12:
			if year > 0:
				if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
					if day <= 31:
						return True
					else:
						return False
				elif month == 4 or month == 6 or month == 9 or month == 11:
					if day <= 30:
						return True
					else:
						return False
				elif month == 2:
					if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
						if day <= 29:
							return True
					elif day <= 28:
							return True
					else:
						return False
				else:
					return False
			else:
				return False
		else:
			return False
	else:
		return False


print(isDateValid(1, 2, 3))
print(isDateValid(0, 0, 0))
print(isDateValid(1, 1, 0))
print(isDateValid(-1, 5, 2000))
print(isDateValid(1, -5, 2000))
print(isDateValid(1, 5, -2000))
print(isDateValid(29, 2, 2020))
print(isDateValid(29, 2, 2021))
print(isDateValid(31, 4, 2021))
print(isDateValid(32, 5, 2021))
