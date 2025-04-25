#### Python Set ####

# Item : Set items are unordered, unchangable, and do not allow duplicate value
fruits = {'apple', 'banana', 'cherry'}
print(fruits)

# Duplicate Value Will be ignored
fruits = {'apple', 'banana', 'cherry', 'apple'}
print(fruits)

# True and 1 are same valu in set and treated as duplicate and ignore one of them
myset = {'abc', 1, True, 'xyz'}
print(myset)

# False and 0 considered as same and ignored one of them
myset = {'apple', 'banana', False, 0, 4}
print(myset)

# Get The Length of a Set
print(len(myset))

# Set Items- Data Type
fruits = {'apple', 'banana', 'cherry'}
num = {2, 3, 4, 5}
myset = {True, False}
price = {2.3, 4.3, 4.2}

# Set With Different Data Type
myset = {'apple', True, 10, 4.5}
print(myset)