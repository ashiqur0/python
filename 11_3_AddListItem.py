#### Add List Item ####

# Append Items
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)

# Insert Items
fruits.insert(1, 'kiwi')
print(fruits)

# Extends List
fruits2 = ['mango', 'pineapple', 'papaya']
fruits.extend(fruits2)
print(fruits)

# Add any Iterable
fruits = ['apple', 'banana', 'cherry']  # List
fruits2 = ('orange', 'kiwi')            # Tupple
fruits.extend(fruits2)
print(fruits)

