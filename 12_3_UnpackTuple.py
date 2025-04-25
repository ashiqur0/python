#### Unpack Tuple ####

fruits = ('apple', 'banana', 'cherry')
red, green, yellow = fruits
print(red)
print(green)
print(yellow)

# Using Asterisk* [the variable with *(asterisk) will contatin the rest of the value when the number of the variable is less than the number of value in a tuple as a list]
red, *green = fruits
print(red)
print(green)

# Add a list of values to the 'tropic' variable
fruits = ('apple', 'banana', 'cherry', 'kiwi', 'orange', 'melon')
green, *tropic, red = fruits
print(green)
print(tropic)   # tropic valiable will store the rest of the variable
print(red)