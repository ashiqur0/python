#### Remove List Item ####

# Remove Specified Item
fruits = ['apple', 'banana', 'cherry']
fruits.remove('apple')
print(fruits)

# When same item multiple time, remove first occurance of banana
fruits = ['apple', 'banana', 'cherry', 'banana']
fruits.remove('banana')
print(fruits)

# Remove Specified Index
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

# Remove the last item
fruits.pop()
print(fruits)

# del keyword also remove the specified index
fruits = ['apple', 'banana', 'cherry']
del fruits[1]
print(fruits)

# del keyword can also use to delete the whole list
del fruits
# print(fruits) # delete the list completely

# clear method is use to remove all the elements of a list
fruits = ['apple', 'banana', 'cherry']
fruits.clear()
print(fruits)   # List still has but it has no elements