
print("Statement\tNumber\t\tAttempt\t\tRemain")

num = 30
atms = 4
rems = 1
while(rems<=6):
	print("\t\t\t\t   "+str(rems)+"\t\t   "+str(atms))
	n=int(input("Input number\t  "))
	if n<num:
		print("Take a higher number next time.")
	elif n>num:
		print("Take a lower number next time.")
	else:
		print("Congratulations! You guessed the number");
		break				
	atms=atms-1
	rems=rems+1
	
if rems==6:
	print("Sorry but you have lost the game. The number you had to guess was", num)



