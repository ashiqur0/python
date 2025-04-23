################ Python Strings ################
# Single quote or double quote strings
print('Hello')
print("Hello")

# Quotes inside Qoutes
print("It's alright")
print('He is called "John"')

# Assign String to a variable
x = "Hello"

# Multiline String
a = """ 
This is 
a multiline 
string
"""
print(a)

# Strings are arrays 
a = "Hello, World"
print(a[0])

# Looping through a string
for x in "banana":
    print(x)
    
# String length
print(len(a))

# Check String
txt = "the best thing in life are free!"
print("free" in txt)

# Use it in if statement
if "free" in txt:
    print("Yes, free in txt")

# Check if NOT
print("expensive" not in txt)

if "awesome" not in txt:
    print("awesome is not in txt")
    
