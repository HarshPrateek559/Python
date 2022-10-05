# In python there is a datatype called set it take value as list or tuple. It store only unique values
s = set([1,2,3,4])
print(type(s))
print(s)
#to add value in set
s.add(5)
print("Updated set after add: ", s)
#to delete values from set
s.remove(1)
print("Updated set after remove: ", s)