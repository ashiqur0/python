#### Access Tuple Item ####

# Access Tuple item by using index number
fruits = ('apple', 'banana', 'cherry','orange', 'kiwi', 'watermelon', 'pineapple')
print(fruits[0])

# Negative Indexing
print(fruits[-1])

# Range of Index
print(fruits[2:5])

# Range from begining to till before the range
print(fruits[:5])

# From the range to end
print(fruits[5:])

# Range of Negative Indexing
print(fruits[-5:-2])

# Check If Item Exist
print('kiwi' in fruits)

if 'apple' in fruits:
    print('Yes. apple is present')
