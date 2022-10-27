#This program is for the file handling capabilities of Python.


"""
These are the modes in which Python opens a file from the computer

"r" : (Read Mode),This mode let python compiler read a file. This is the default mode

"w" : (Write Mode),This mode let python compiler write to the file. It overwrites whatever data is present in the file

"x" : (Exclusive mode), This mode create a file in the system only if there is no other file of the same name and type

"a" : (append mode),This mode is used to add something to the end of the file. This mode do not overwrite and neither have the permission to read a file

"t" : (text mode), This mode is used to open proper text file

"b" : (Binary mode), This mode is used to open file in binary mode. Files in this mode read new lines as "\n" and tab space as\t

"+" : (plus mode), In this mode a file can be read and written at the same time

"""

#To open a file use open("file path","mode")
#f.seek(integer)-this function takes the pointer to the pointer location given by the integer
#f.tell()-This function returns the current location of pointer in the text file.

def writing():
	n = input("Type what you want to add in the text file\n")
	print("\n")
	f = open("D:\Software Development\Python\Python Basics\FileIO\\text.txt","a+")#If i append on a file and then close it then again open the file and read it then the inputted text will be displayed in the same runtime
	f.write("\n"+n)
	f.close()
	reading()
	
def reading():
#	f = open("text.txt","r+")to use "b" you have to use "rb" or "wb" or "ab". "r+" and "a+" let user to read and write 
	with open("D:\Software Development\Python\Python Basics\FileIO\\text.txt","r+") as f:
		content = f.readlines()#read, readline and readlines take int argument which is the number of character they have to read
	
		for lines in content:
			print(lines,end="")
	print()
#after operations you have to close the file
#	f.close() with block do not require close statement
	
try:
	flag = True
	while (flag):
		ch = input("Do you want to make change in the file or not y/n: ")
		if(ch=="y"):
			writing()
		else:
			reading()
		c = input("\nDo you want to do it again y/n: ")
		if c=="y":
			flag = True
		else:
			flag = False
except Exception as e:
	print(e)