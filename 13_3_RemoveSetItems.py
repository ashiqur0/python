#### Remove Set Items ####

# remove() method
fruits = {'apple', 'banana', 'cherry'}
fruits.remove('apple')      # if the item doesn't exist the remove() rise an erro.
print(fruits)

# discard() method
fruits.discard('cherry')    # if the item doesn't exist the discard() will not rise an error
print(fruits)

# pop() method : will remove a random item
fruits.pop()
print(fruits)

# del keyword : delete the set completely
del fruits
# print(fruits)

# clear() method : remove all the item from a set
fruits = {'apple', 'banana', 'cherry'}
fruits.clear()
print(fruits)