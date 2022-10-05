#this program is an example of break and continue in while loop




#It is a special kind of loop which will run forever
while(True):
	i = int(input("To stop the loop, give the input of greater than 100 otherwise less than 100: "))
	if i<100:
		continue #This statement will ignore the statements under it and will start a new iteration of the loop.
		print("You have entered a value of: ")
	break #This statement will break and exit the loop 
	print("This statement will never execute")

print("Congratulations! You have exited the loop with value of ", i)
