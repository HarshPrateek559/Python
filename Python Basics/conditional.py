#conditionals
list = [5,6,7,8,9,10]
if 5 in list:
	print("Yes 5 is included")# in keyword is a way to check if the data structure is includes the value
elif 100 not in list:
	print("No 100 is not in list")#not in keyword check if the structure not include the value

age = int(input("Please tell us your age: "))

if 1<age<100:
	if age<18:
		print("At the age of %d you cannot drive. Come back later." % age)
	elif age==18:
		print("Congrats! You have turned 18 so you have to come and give your driving test.")
	else:
		print("At age of %d you should definitely drive and you don't need a driving test for it." %age)

else:
	print("Please give a valid age")