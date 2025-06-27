# while loop

"""
while condition:                # this is the syntax of while loop in python.
    statements

"""

# break and continue are same as in c++.


# FOR LOOPS

list = [2,5,6,1]            # this is how you can traverse a list or tupple.
for el in list:
    print(el)

# for loops with else statement.
for el in list:
    print(el)
else:
    print("Loop Ended")             # works when loop has ended.agar loop break hua then else statement will not run, this statement will run only when loop has finished properly.


# range function
# range(n) function returns a sequence of numbers starting from 0, increment of 1 by default, and 1 less than the given argument tak run hota hai.
# general syntax->
# range(start?, stop, step?)        # question mark waale optional hote hai.

for i in range(5):      # only one argument so this is stop parameter.
    print(i)

for i in range(1,5):     # two parameters start and stop
    print(i)

for i in range(1,5,2):   # now step is also included.
    print(i)


# pass in loop
for i in range(4):          #  agr hum kisi loop me kuchh nhi karna chahte then we use pass statement, iski jarurat isliye padi because
    pass                    #  if pass nhi likhoge and loop ke baad kuchh karne jaaoge to python will throw an error ye samajh ke ki tum usko for loop ke ander likhna bhul gye.
print("is loop me kuchh nhi karna")
