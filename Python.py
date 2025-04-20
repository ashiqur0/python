#################### Structured way to Learn Python ####################

# # First Program in Python
# print("Hello, World!")

# #################### Python Syntax ####################
# # Python Indentation 
# if 5 > 2:
#     print("Five is greater than two")

# # Python Variables
# x = 5
# y = "Hello World!"

# # Comments

#################### Python Comments ####################
# This is a comments
"""
This is a multiline
comments
"""

'''
this is also a 
multiline comments
'''

#################### Python Variables ####################
# Creating Variable
x = 5
y = "John"

# Type Casting 
x = str(3)
y = int("3")
z = float(3)

# # Get The Type
# print(type(x))

# Single or Double Quote
x = "John"
x = 'John'

# Case Sensitive
a = 5
A = "Antana"

# Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# # Illigal Variable
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Multi Words Variables
myVariableName = "John"     # Camel Case
MyVariableName = "John"     # Pascale Case
my_variable_name = "John"   # Snake Case

# Assign Multiple Values
# Many Valu to Multiple Variables
x, y, z = "apple", "banana", "cherry"

# One value to multiple variables
x = y = z = "apple"

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

# Output Variables
# print(x)

x = "Python"
y = "is"
z = "awesome"
# print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
# print(x + y + z)

x = 5
y = 10
# print(x + y)

x = 5
y = "John"
# print(x + y) # Error: different data element can't be concat
# print(x, y)

# Global Variable 
x = "awesome"
# def myfun():
#     print("Python is " + x)   
# myfun()

x = "awesome"
def myfun():
    x = "fantastic"
    # print("Python is " + x)
myfun()
# print("Python is " + x)

# global Keyword (can make a scope variable to global variable)
def myfun():
    global x
    x = "awesome"
myfun()
# print("Python is " + x)

# Change value inside of a function 
x = "awesome"
def myfun():
    global x
    x = "fantastic"
    # print("Python is " + x)
myfun()
# print("Python is " + x)