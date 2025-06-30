
#Reduce():  It is a function that simplifies a list or sequence into a single value by applying a specific function to its elements
#           This function is defined in "functools" module.

# syntax:
            # from functools import reduce
            # reduce(function, iterable,initializer)


#  Concatenating Strings
from functools import reduce
strings = ["Hello", " ", "World", "!"]
concatenated = reduce(lambda x, y: x + y, strings)
print(concatenated)  

#calculating  Sum of tuple element with initial value
from functools import reduce
myNumbs = (2, 4, 6)
print(reduce(lambda x, y: x+y, myNumbs, 8))

#calculate sum of all list element
from functools import reduce
l=[1,2,3,4,5,6,7]
sum=reduce(lambda x,y:x+y,l)
print(sum)

#filter odd no from this list add this odd element
l=[1,2,3,4,5,6,7,8,9]
a=filter(lambda x:x%2!=0,l)
b=reduce(lambda x,y:x+y,a,2)
print(b)





