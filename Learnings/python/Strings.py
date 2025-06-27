# syntax of string
# strings are immutable datatypes in python (not changable)

# str1 = 'this is a string'
# str2 = "this is also a string"
# str3 = """you won't believe but this is also a string"""

# print(str1)
# print("\n")           this is how we print a next line in python. 
# print(str2,"\n",str3)


# Concatenation
"""
str1 = "Anish"
str2 = "Patel"

print(str1 + " " + str2)        # Anish Patel

"""


# fun to find length of string.
"""
str = "Anish"
size = len(str)
print(size)

"""


# 0 base indexing in python.
# it has negative indexing also, with -1 from last character to decreasing while coming towards starting point.
# you can access char from index, but you can't manipulate/change/assign the data.

# SLICING
# last number is not included in slicing.
# general formula/syntax           str(starting_idx : ending_idx)
"""
str = "Anish Patel"
print(str[1 : 4])               # this will print "nis"
print(str[0 : 5])               # this will print "Anish"
print(str[ : 5])                # same as above.
print(str[1 : ])                # 1 se lekar end tak print kar dega "nish Patel"

"""

# there are many inbuilt functions in python, we can use them if we want. For example :-
# just type "str."  and python will automatically suggest you its inbuilt functions.
"""
str = "anish"
print(str)
str = str.capitalize()          # to capitalise the first letter of the string, It doesn't do changes in the original string.      
print(str)                      # if we want we can save the changes in the str as done above.

"""
