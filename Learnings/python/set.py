# unordered, immutable, unique entries
# can add any datatype other than list and dictionary 

num = {1,2,3,"anish","patel",2}         # will ignore duplicate entries
print(num) 
print(type(num))
print(len(num)) 

name = {"anish","akhil","rohit","ishant"}
marks1 = {60,98,78,69}
marks2 = {43,98,69,1}

# empty set
null_set = set()                # because "{}" this would count into dictionary and "()" this in tupple.
print(type(null_set))

# Some functions
num.add("college")          # adds the element in set.(one argument at a time)
print(num)

num.remove(3)               # removes the element
print(num)

num.pop()                   # removes a random element
print(num)

num.clear()                 # empties the set
print(num)         

union = name.union(marks1)           # marks ko name me daal ke kisi aur set ko assign kar dega. (following the basic rules of set)
print(name)                     # no change will be there in name set.
print(union)

common = marks1.intersection(marks2)
print(common)