
# filter() :1)The filter() method filters the given sequence with 
#           the help of a function that tests each element in the sequence to be true or not
#          2)It returns an iterator that contains all the elements of the
#            input iterable that have passed the function check.


# Syntax: filter(function, sequence)
#           function - a function that runs for each item of an iterable
#            iterable - a sequence that needs to be filtered like sets, lists, tuples, etc



#filtering out items that correspond to none
test = [1, 5, 0, True, "", -1, -45, False, 0.0, {}, (), []]
filtered_list = filter(None, test)
print(list(filtered_list))


#sorting a list of dictionaries based on price which is greater than 10
d= [
   {"Item":"Pen", "Price":50},
   {"Item":"Pencil", "Price":10},
   {"Item":"Notebook", "Price":80},
   {"Item":"Eraser", "Price":10}
   ]

filtered_items=filter(lambda x:x['Price']>10,d)
print(sorted(filtered_items,key=lambda x:x['Price']))


# #filter even number
l=[1,12,2,23,4,54,7,9,23,-1]
a=filter (lambda x:x%2==0,l)
print(list(a))


# #filter positive number
b=filter(lambda x:x>=0,l)
print(list(b))

# #create list of string and filter string which length is greater than 3
# l=['abc','asdf','qwer','as','uyt']
# a=filter (lambda x:len(x)>3,l)
# print(list(a))

#to sort list of dictionary 
# l=[{'Name':'vbbh','age':24},{'Name':'asdw','age':12}]
# a=sorted(l,key=lambda x:x['Name'])
# print(a)

# take list and calculate average of all elements 
# l=[1,2,3,4,5,6,6,7,8]
# a=(sum(l)/len(l))
# print(a)
# b=filter(lambda x:x>a,l)
# print(list(b))

#list of dict in which key 1.item 2.price 
l=[{'item':'apple','price':40},
   {'item':'banana','price':30},
   {'item':'mango','price':100}
   ]
a=sorted(l,key=lambda x:x['price']*0.5)
print(a)




