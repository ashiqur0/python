#### Python Lambda ####

# add 10 to the argument a and return the result
x = lambda a : a + 10
print(x(10))

# Multiply argument a with agrument b and return the result
y = lambda a, b : a * b
print(y(2, 3))

# Summarize argument a, b, c and return the result
z = lambda a, b, c : a + b + c
print(z(2, 3, 4))

# inside a function that always double the number
def myfun(n):
    return lambda a : a * n

mydobler = myfun(2)
print(mydobler(11))

# a function that always tripple the number
mytripller = myfun(3)
print(mytripller(11))

