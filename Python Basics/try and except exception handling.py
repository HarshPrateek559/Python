#This Python program is for try except exception handling. Whenever an exception occur in the program it will handle the error message and print it in the console and let rest of the program to execute. 

i = input("Enter a number:")

try:
	sum = i+6
except Exception as e:
	print("\nError:",e)#datatype of e is TypeError
	
	
print("\nWithout try except this line will not execute because of the error message")