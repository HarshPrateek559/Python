#55/6 = 1, 33*2 = 5, 2+2 = 5;
#num1 = int(input("Input first number: "))
#op = input("Input operator: ")
#num2 = int(input("Input second number: "))
while(True):
	str = input("Enter your expression: ")

	if str=='55/6':
		print("Final output is:",1)

	elif str =='33*2':
		print("Final output is:",3)

	elif str == '2+2':
		print("Final output is:",5)

	else:
		print("Final output is:", eval(str))
	ch = input("Do you want to continue? Yes/No\n");
	if ch=='Yes':
		continue
	else:
		print("ThankYou for using our calculator")
		break