# print("anish")            // syntax to print anything.

'''
if(condition):          # if else, here indentation is very imp, a "tab" is the indentation for if else condition.
    statements
elif(condition):
    statements
else:
    statements

'''

# python is an implicit language, that means that we don't need to specify the type of data which we are declarying.
'''
name = "anish"          #str
age = 20                    # int
percentile = 98.63              #float

'''


# taking input from the user
'''
A = input("enter the value of A : ")        # this statement will take input from user and assign datatype string to it.
B = int(input("enter the value of B : "))  # we have already told python to make A an int datatype

print(A)            # this will print whatever user has given as data
print(type(A))      # this will print the datatype of "A"
print(B)
print(type(B))

'''

# single line if else statement(ternary operator)
'''
food = input("enter your favourite food : ")
isFavourite = True if food == "DalBhatChokha" else False        # var1 = <val1> if <condition> else <val2>
print(isFavourite)
print(type(isFavourite))            // bool

# or instead of value we can give statements to run also, eg:
food = input("enter your favourite food : ")
print("sweet") if food == "cake" else print("not sweet")        # <stt1> if <condition> else <stt2>

# clever if
age = input("enter age: ")
vote = ("No", "Yes") [int(age) >= 18]       <var> = (false_value, true_value)[<condition>]     #condition false hone per first value would be assigned to var1.
print(vote)

'''


# type casting
'''
a = "2"
a = int(a)      # "a" got type casted into int from string.
print(a)
print(type(a))

'''


