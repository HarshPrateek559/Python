#This is an attempt to make a linear search program
li = [1,4,2,6,88,39,102,334,857,9762,1000,100,101,394,444,448,257]
li.sort()
flag = True
while(flag):
	n = int(input("Give a number to be searched in the list: ")
	c =0
	f=0
	for i in li:
		c+=1
		if(n==i):
			f=1
			print("%d is in the position %d in the list" %(n,c))
	if(f==0):
		print("Sorry the number %d is not in the list" %(n))
	p = input("Do you want to keep looking? Yes/No: ")
	if(p=="No"):
		flag = False