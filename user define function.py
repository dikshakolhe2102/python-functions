# nested function
# def outer():
#     def inner():
#         print("Inner")
#     print("Outer")
#     inner()
# outer()

#Recursion Function
def f1(n):
    print(n)
    if (n==10):#Base case
        return
    f1(n+1)#recursive case
f1(0)

#User defined function :1)A User-Defined Function (UDF) is a function created by the user to perform specific 
#                           tasks in a program.
#                       2)It allows for code reusability and modularity, making programs easier to read
#                             and maintain.
# 3)Syntax of User defined Functions
# Function Defination:
                # def function_name(parameters):
                #        Function body
                #        return result
# Function Call:
                # function_name(arguments)

#Return statement :  1)It ends the function execution.
                #    2)It send back a result (value or multiple values) to where the function was called.
                #    3) Any code written after the return will be ignored 

#Types of User defined functions:
# 1)Function with no arguments and no return value
def f1():
    print("In function f1")
    print("Function with no arguments and no return value")
print("Out of funtion")
f1()

# 2)Function with no arguments and return value
def f2():
    print("Function with no arguments and return value")
    return "Hello from f2"
result=f2()
print(result)  

# 3)Function with arguments and no return value
def f3(name):
    print("Function with arguments and no return value")
    print(f"Hello, {name}!")
n=input("Enter your name: ")
f3(n)

# 4)Function with arguments and return value
def f4(name):
    print("Function with arguments and return value")
    return f"Hello, {name}!"
n=input("Enter your name: ")
print(f4(n))

# 5)Function with default arguments
def f5(x=20):
    print("Function with default arguments")
    print(f"Value of x is: {x}")
f5()  # Calling with default value
f5(30)  # Calling with a different value

# 6)Function with multiple return values
def f5():
    print("Function with multiple return values")
    return 10, 20, 30

a, b, c = f5()
print(f"Returned values: a={a}, b={b}, c={c}")

#EX2
def f6(a, b):
    print("Function with multiple arguments")
    return a + b, a - b, a * b, a / b
x= int(input("Enter first number: "))
y= int(input("Enter second number: "))
print("Results of f6: ", f6(x, y))

#Ex3
def f7(s):
    a=len(s)
    b=s[0]
    c=s[::-1]
    return a,b,c
s=input("Enter a string : ")
result=f7(s)
print("String Operation : ", result)

#7)Function with  Keyword Argument: arguments are assigned based on the name of the arguments
def display(x,y):
    print('Value of x:', x)
    print('Value of y:', y)
display(y = 100, x = 20)

#8)Function with mulitiple argument(*args) : Accepts multiple values as a tuple.
def add(*args):
    print(args[0]+args[1])
    print(sum(args))
add(1, 2, 3, 4)


#9)Function with Keyword Arguments using **kwargs : Accepts named arguments as a dictionary.
def display(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
display(name="ABC", age=25, city="Nagar")


#Positional vs Keyword Parameters
def f1(x,y):
    print(f"{x}, {y}!")
#Positional
f1(10,20)
#Keyword
f1(y="Hi", x="Python")

#ALL in One
def example(a, b=2, *args, **kwargs):
    print("a =", a)
    print("b =", b)
    print("args =", args)
    print("kwargs =", kwargs)

example(1, 3, 4, 5, x=10, y=20)






