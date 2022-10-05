#in python a function is defined by def keyword and returns a value by return keyword.
"""
def recursion(n):
	if (n<=1):
		return 1
	return n*recursion(n-1)

n = int(input("Enter a number to find factorial: "))
print("Factorial of %d is: "%n,recursion(n))
"""
def fabinocci(x):
	x1,x2 = 0,1
	print("Fabinocci series is: ", end = " ")
	for i in range(0,x):
		print(x1, end=" ")
		x3 = x1+x2
		x1 = x2
		x2 = x3
x = int(input("Enter the number of elements in fabinocci series: "))
fabinocci(x)