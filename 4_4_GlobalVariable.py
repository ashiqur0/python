#### Global Variable ####

# Create a variable outside of a function
x = "awesome"
def myfun():
    print("Python is " + x) 

myfun()

# Create a variable inside of a function
x = "awesome"
def myfun():
    x = "fantastic"
    print("Python is " + x) # Python is fantastic

myfun()
print("Python is " + x)     # Python is awesome

# 'global' keyword : Let the scope variable to access from outside of the method 
def myfun():
    global x
    x = "fantastic"
myfun()
print("Python is " + x)     # Python is fantastic

# Change a global variable inside of a function
x = 'fantastic'
def myfun():
    global x
    x = "awesome"
myfun()
print("Python is " + x)     # Python is awesome