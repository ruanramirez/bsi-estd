def fibo(n):
	if n == 0:
		return 0
	else:
		if n == 1:
			return 1
		else:
			return fibo(n-1) + fibo(n-2)

print(fibo(0), fibo(1), fibo(2), fibo(3), fibo(4), fibo(5), fibo(6), fibo(7), fibo(8))
