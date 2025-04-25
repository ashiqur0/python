#### Python Tuple ####

# Tuple Creation
mytuple = ('apple', 'banana', 'cherry')
print(mytuple)

# Tuple Item
print(mytuple[0])
print(mytuple[1])

# Ordered, Unchangable, Allow Duplicates
mytuple = ['apple', 'banana', 'cherry', 'apple', 'cherry']
print(mytuple)

# Tuple length
print(len(mytuple))

# Create Tuple with one Item
mytuple = ('apple',)
print(type(mytuple))    # tuple

mytuple = ('apple')
print(type(mytuple))    # Not a tuple

# Tuple Items - Data Type
tuple1 = ('apple', 'banana', 'cherry')
tuple2 = (3, 2, 4, 1, 0, 5)
tuple3 = (True, False, True, False)

# Tuple with Different Data Type
tuple1 = ('abc', 4, True, 23.2, 4+3j)

# Get the Data Type
print(type(tuple1))

# The tuple() Constructor
tuple1 = tuple(('apple', 'banana', 'cherry', 'orange'))
print(tuple1)