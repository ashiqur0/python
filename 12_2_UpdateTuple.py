#### Update Tuple ####

# Change Tuple Value (Tuple is unchangable. You can not add, remove, or update tuple directly)
fruits = ('apple', 'banana', 'cherry', 'kiwi', 'melon')
x = list(fruits)
x[0] = 'orange'
fruits = tuple(x)
print(fruits)   # orange instead of apple

# Add Item
x = list(fruits)
x.append('watermelon')
fruits = tuple(x)
print(fruits)

# Add Tuple to a Tuple
fruits1 = ('apple', 'banana', 'cherry')
fruits2 = ('orange', 'kiwi', 'melon')
fruits1 += fruits2
print(fruits1)

# Remove Item
fruits = ('apple', 'banana', 'cherry')
x = list(fruits)
x.remove('apple')   # remove() method remove specific item from a list
fruits = tuple(x)
print(fruits)

x.pop()             # pop() method remove last element from the list
fruits = tuple(x)
print(fruits)

x.pop(0)            # pop(index) method remove the indexed item from the list
fruits = tuple(x)
print(fruits)

del fruits
# print(fruits)     # del keyword can delete a tuple completely

fruits = ('apple', 'banana', 'cherry')
x = list(fruits)
x.clear()           # clear method remove all the elements from a list
fruits = tuple(x)
print(fruits)