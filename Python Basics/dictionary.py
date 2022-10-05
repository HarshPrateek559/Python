#in python a key value pair is a dictionary rest everything is same as js
dict = {
1:"first",
2:"second",
3:"third",
4:"fouth"
}
print(dict)
#to add another key value pair in dictionary
dict[5] = "fifth"
print(dict)
for i in dict:
	print(dict[i])
#to delete a key value pair in python
del(dict[1])
#print("\n")
print(dict)
