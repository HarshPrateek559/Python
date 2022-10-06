def fibonacci(n):
	a, b = 0, 1
	print(0,1,end=" ")
	for i in range(n):
		c=a+b
		if c is not None:
			print(c,end=" ")
		a = b
		b = c
		
print("Fibonacci sequence is:",end = " ")
print(fibonacci(8))		