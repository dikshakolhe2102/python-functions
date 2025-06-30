
#map() :1)The map() function is used to apply a given function to
#       every item of an iterable, such as a list or tuple, and returns a map object
#      2) The map() function returned an iterator, which we then converted into a list using list().


#syntax: map(function, iterable)

#calculating double of each number in a list using map function
a= [1, 2, 3, 4]
result = list(map(lambda x: x * 2, a))
print(result)

# Using map() with multiple iterables
a = [1, 2, 3]
b = [4, 5, 6]
result = map(lambda x, y: x + y, a, b)
print(list(result))


#convert a list element to integer
s = ['1', '2', '3', '4']
result= map(int, s)
print(list(result))


l=[{'item':'apple','price':40},
   {'item':'banana','price':30},
   {'item':'mango','price':100}
   ]
a=map(lambda x:x['price']*0.5,l)
print(list(a))

# sorted age
l=[{'info':{'age':21}},
   {'info':{'age':19}},
   {'info':{'age':30}},
   {'info':{'age':10}}]
a=sorted(l,key=lambda x:x['info']['age'])
print(a)



# map used when the complete elements are you want to change
# filter is used when you want to filter items
# lambda is used when you want to use one line function


# given alist of string 1. filter out string less than 5
#then convert remainimng string to the uppercase string using map and filter string
l=['ab','qwertyui','asdfghjk','gfds','fcvcjc']
a=filter(lambda x:len(x)<5,l)
print(list(map(lambda x:x.upper(),a)))