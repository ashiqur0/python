#### List Comprehension ####

# Copy list elements which contains 'a' letter 
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = []
for x in fruits:
    if 'a' in x:
        newlist.append(x)

print(newlist)

# Using List Comprehension
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = [x for x in fruits if 'a' in x ]
print(newlist)

# Only accept that are not apple
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = [x for x in fruits if x != 'apple']
print(newlist)

# With no if
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = [x for x in fruits]
print(newlist)

# Iterable
newlist = [x for x in range(10)]
print(newlist)

# Accept only the number less than 5
newlist = [x for x in range(10) if x < 5]
print(newlist)

# See the value in new list upper case
newlist = [x.upper() for x in fruits]
print(newlist)

# Set all the value in new list to hello
newlist = ['hello' for x in fruits]
print(newlist)

# Return orange insted of banana
newlist = [x if x != 'banana' else 'orang' for x in fruits]
print(newlist)