#### Python For Loop ####

# Print each fruits from fruits list
fruits = ['apple', 'banana', 'charry']
for x in fruits:
    print(x)

# Looping Through a String
for x in 'apple':
    print(x)

# The Break Statement
for x in fruits:
    print(x)
    if x == 'banana':
        break

# The continue Statement
for x in fruits:
    if x == 'banana':
        continue
    print(x)

# The range() function
for x in range(5):      # Default strt from 0
    print(x)

for x in range(2, 7):   # Using start parameter
    print(x)

# Else in Fore loop
for x in range(5):
    print(x)
else:
    print('Finally finished')

# Break The Loop When x is 3, and see what happen
for x in range(5):
    if x == 3:
        break
    print(x)
else:
    print('Finally Finished')

# Nested Loop
adjective = ['red', 'big', 'tasty']
fruits = ['apple', 'banana', 'cherry']
for x in adjective:
    for y in fruits:
        print(x + " " + y)

# The pass Statement
for x in range(5):
    pass