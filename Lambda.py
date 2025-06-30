
#lambda function:1)A lambda function is a small anonymous function defined using the lambda keyword. 
#                2)It's typically used when you need a short function for a short time — especially as 
#                  an argument to higher-order functions.
#                 3)A lambda function can take any number of arguments, but can only have one expression.
                  #4)It will return a single value.

# Syntax : lambda arguments: expression

#function with no parameter and no return type
f1=lambda :print("Python")
f1()

#function with no parameter and return type
f2=lambda : "Python"
print(f2())

#function with one parameter and no return type
f3=lambda x: print(x)
f3("Python")

#function with one parameter and return type
f4=lambda x: x*2
print(f4(7))

#function with  varaible parameters
f5=lambda *args: print("Sum of arguments is :",sum(args))
f5(5,10,3,4,9)

#function with  Keyword arguments 
f6=lambda **args: print("Sum of arguments is :",sum(args.values))
f6(a=7,b=7,c=9,d=10)

#lambda function in one line
print((lambda x:x**2)(2))

# Check if a number is even or odd using a lambda function
check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(4))  
print(check(7))



#sorting a list of dictionaries based on price
d= [
   {"Item":"Pen", "Price":50},
   {"Item":"Pencil", "Price":10},
   {"Item":"Notebook", "Price":80},
   {"Item":"Eraser", "Price":10}
   ]

print(sorted(d,key=lambda x:x['Price']))

# #by default return return statement
# #it is anonomus function

#even odd no using lambda function
num=int(input("Enter no:"))
result=lambda x:print("Even") if(x%2==0)else print("odd")
result(num)

