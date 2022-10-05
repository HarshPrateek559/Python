duct = {
  "Javascript" : "frontEnd",
  "Python" : "ML and AI",
  "Java" : "android development",
  "Cpp" : "executables"
}

n = input("Enter a word to find in dictionary: ").capitalize()
c=0
for i in duct:
	if(n==i):
		c+=1
if(c==1):
	print(duct[n])
else:
	k = input("This word is not in the dictionary. If want to add type yes otherwise no.\n")
	if(k=="yes"):
		d = input("Please give us the meaning of this word\n")
		duct[k]=d
		print("We have added your word to the dictionary.")
		print("Updated Dictionary: ", duct)
	else:
		print("We are sorry to hear that! We will not add this word to our dictionary.")