# this program will convert decimal to binary
flag = True
while(flag):
    d = int(input("Please enter a number in decimal: "))
    s = bin(d).removeprefix("0b")
    print("The binary equivalent of %d is %s" %(d,s))
    ch = input("Do you want to continue.Y/N: ")
    if(ch=="Y" or ch=="y"):
        flag=True
    else:
        flag=False
