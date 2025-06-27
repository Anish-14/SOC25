# stores key value pairs
# unordered, mutable, don't allow duplicate keys , (keys can be anything accept list)
# this is the syntax to create a dictionary.

"""
student = {
    "name" : "Anish Patel",         # "name" is key and "Anish Patel" is it's value.
    "class" : 12,
    "roll no" : 24
}

print(student["name"])               # prints the value associated to "name" key.
print(student)                       # prints the whole dictionary

student["name"] = "Mukul Gupta"         # can change a value associated to the key.
student["age"] = 20                     # can add a new key value pair.

print(student)

"""

# NULL Dictionary
my_dict = {}


# Nested dictionary"

student = {                    # there's a dictionary inside a dictionary.
    "name" : "Dev Kumar",
    "subjects" : {
        "phy" : 93,
        "math" : 97,
        "chem" : 95
    }
}

print(student)                             # prints the whole dictionary for us.
print(student["subjects"])                 # prints the dictionary "subjects"
print(student["subjects"]["phy"])          # prints 93


# Some functions
print(len(student)) 
print(student.keys())           # returns all the keys present in the dict.
print(student.values())         # returns all the values present in th dict.
print(student.items())          # returns all (key,value) pairs as tupple
print(student.get("name"))      #returns the value of key

student.update({"city" : "Delhi"})          # this key value pair got updated/added in the dict.
print(student)
new_dict = {"country" : "India" , "age" : 16}            # we can make a new dict also and then add it to any other dict.
student.update(new_dict)
print(student)
new_dict1 = {"name" : "Anish Patel"}            # if any common key found, then that key value pair gets updated.
student.update(new_dict1)
print(student)