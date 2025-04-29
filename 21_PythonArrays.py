
#### Python Arrays ####

# Create an Array
car = ['Ford', 'Volvo', 'BMW']

# Access the element of an Array
x = car[0]

# Modify the value of the first item
car[0] = 'Toyota'

# The length of an array
length = len(car)

# looping array elements
for x in car:
    print(x)

# Adding array element
car.append('Ford')
print(car)

# Removing array element
car.pop()
print(car)

# remove() method
car.remove('BMW')
print(car)

#### Array Methods ####
# append() method : adds an element at the end of the list
fruits = ['apple', 'banana']
fruits.append('cherry')
print(fruits)

# clear() method : remove all the elements from the list
fruits.clear()
print(fruits)

# copy() method : returns a copy of the list
fruits = ['apple', 'banana', 'cherry']
fruits2 = fruits.copy()
print(fruits2)

# count() mehod : returns the number of elements with the specified value
car = ['Tesla', 'Volvo', 'Tesla', 'BMW', 'Tesla']
x = car.count('Tesla')
print(x)

# extend() method : add the element of the list (or any iterable) to the end of the list
color = ['red', 'white']
color2 = ['yello', 'black']
color.extend(color2)
print(color)

# index() method : returns the index of the first element with the specified value
num = [2, 3, 4, 2, 4, 2, 6]
x = num.index(2)
print(x)

# insert() method : Adds an element at the specified position. example: car.insert(2, 'Tesla')
fruits = ['orange', 'cherry', 'kiwi']
fruits.insert(0, 'apple')
print(fruits)

# pop() method : remove the element at the specified position
animale = ['Lion', 'Tiger', 'Elefent']
animale.pop()
print(animale)

# remove() method : remove the first item with the specified value
price = [2.9, 3.0, 4.8]
price.remove(2.9)
print(price)

# reverse() method : reverse the order of the list
num = [4, 5, 6, 7, 8, 9]
num.reverse()
print(num)

# sort() method : sort the list
num = [10, 2, 8, 3, 5, 7, 4, 1]
num.sort()
print(num)