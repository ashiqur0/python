################ Python Booleans ################

# Boolean Value 
print(9 < 10)
print(9 == 10)
print(9 > 10)

# Print message based on weather the condition is true or false
a = 3
b = 4
if a > b:
    print("a is grater")
else:
    print("b is grater")
    
#### Evaluates values and variable ####
# Evaluate string and number
print(bool("Hello"))
print(bool(4))

# Evaluate variable
x = "Hello"
y = 4
print(bool(x))
print(bool(y))

# Most values are true 
print(bool("abc"))
print(bool(123))
print(bool(["apple", "banana", "cherry"]))

# Some values are false
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# Function can return a boolean
def myfun():
    return True
print(myfun())

# Print if the function return Ture 
if myfun():
    print("Yes")
else:
    print("No")

# Check if an object is an integer or not
x = 4
print(isinstance(x, int))