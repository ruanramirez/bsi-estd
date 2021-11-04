def isPalindrome(string):
	string = string.lower()
	if len(string) < 2:
		return True
	if string[0] != string[-1]:
		return False

	return isPalindrome(string[1:-1])


print(isPalindrome('anna'))
print(isPalindrome('anNa'))
