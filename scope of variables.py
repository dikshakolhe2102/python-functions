# #local scope
# def f1():
#     y=20
#     print(y)
# f1()
# #print(y)

# #global scope
# a=10
# def f2():
#     a=20
#     print("Local value of a:",a)
# f2()
# print("global value of a:",a)

# #global keyword
# a =10
# def f2():
#     global a
#     a+=2
#     print('Local value of a : ', a)
# f2()
# print('Global value of a : ', a)


# #enclosing scope (Nonlocal)       
# def outer_funtion():
#     z=30
#     def inner_function():
#         print(z)
#     inner_function()
# outer_funtion()
# #print(z)    

# a=10
# def f1():
#     a=20
#     def f2():
#         nonlocal a
#         a=+2
#         print(a)
#     print(a)
#     f2()
# f1()
# print(a)

# passing inmutable parameter in function(passed value)
# def f1(a):
#     a=a.lower()
#     print(a)
#     print(id(a))
# x='python'
# f1(x)
# print(x)
# print(id(x))


#passing a mutable parameter in function(passed reference)
# def f1(a):
#     a.append(6)
#     print(a)
#     print(id(a))
# x=([1,2,3,4])
# f1(x)
# print(x)
# print(id(x))


#Scope of the variable
# A variable scope specifies the region where we can access a variable.
# Based on the scope, we can classify Python variables into three types:
# 1) Local Variables
# 2)Global Variables
# 3)Nonlocal Variables


# Local Scope: Variables defined inside a function have local scope. 
            # They are accessible only within that function and are not visible outside of it. 
def f1():
      y = 20 
      print(y)
f1() 
#print(y)         # NameError: name 'y' is not defined


#Global Scope: Variables that are defined outside of any function or class have global scope.
#              This means they can be accessed from anywhere within the program. 

a =10
def f2():
    # a=20
    print('Local value of a : ', a)
f2()
print('Global value of a : ', a)

#Global Keyword: In Python, the global keyword allows us to modify the variable outside of the current scope.
            #        global keyword is used  to modify a global variable inside a function.

a =10
def f2():
    global a
    a+=2
    print('Local value of a : ', a)
f2()
print('Global value of a : ', a)


# Enclosing Scope (Nonlocal): In Python, if a variable is defined in an enclosing (outer) function and 
#                             accessed in an inner function, it is referred to as an enclosing or nonlocal variable.

def outer_function():
      z = 30 # Enclosing variable
      def inner_function():
         print(z) 
      inner_function()
outer_function()     # Output: 30
#print(z)            # Error: NameError: name 'z' is not defined



