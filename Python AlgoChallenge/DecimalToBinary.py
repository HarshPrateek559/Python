# this program will convert decimal to binary
flag = True
while(flag):
    print("\n")
    d = int(input("Please enter a number in decimal: "))
    s = bin(d).removeprefix("0b") #This function converts decimal number to binary.76
    print("The binary equivalent of %d is %s" %(d,s))
    ch = input("Do you want to continue.Y/N: ",)
    if(ch=="Y" or ch=="y"):
        flag=True
    else:
        flag=False
