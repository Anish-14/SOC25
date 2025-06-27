# just as list but immutable


tup = ()        # this is a tupple with no elements
tup2 = (2,)     # whenever creating a tupple with single element always end it with a comma else python will think it as an integer value.


tppl = (67,6,1,9,6,1)
element = tppl[0]
print(element)
print(tppl.index(1))       # returns the index of given element occured first time
print(tppl.count(6))       # counts the total occurance of given element.
