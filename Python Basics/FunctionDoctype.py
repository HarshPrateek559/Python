#Any multiLine comment in the first line of a function is its doctype. This can be called for builtin as well as user defined function

print(sum.__doc__)
print("\n"+str.capitalize.__doc__)#here the syntax of capitalize was string.capitalize so we had to do that accordingly
#Here print doc statement is giving error so we have to use it after defining the function
#print("\n"+aver.__doc__)

def aver(a,b,c):
	"""This function returns the average of three numbers"""
	avg = (a+b+c)/2
	return avg
print("\n"+aver.__doc__)