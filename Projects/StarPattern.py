num = int(input("Enter a digit between 0 to 9 for repeating pattern: "))
n = int(input("Enter the number of rows: "))
slope = int(input("Enter 0 for down slope or 1 for up: "))
j = 1
if slope and 0<num<10:
	for i in range(1,n+1):
		for i in range(0,j):
			print(num,end="")
		j+=1
		print("")
		
elif not slope and 0<num<10:
	for i in range(1, n + 1):
	#	for i in range(0,j):
	#		print("",end="")
		for i in range(0, n - j + 1):
			print(num,end = "")
		j += 1
		print("")
else:
	print("Enter a one digit number only")