#### Remove Dictionary Item ####

# Remove Item
car = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
print(car)

# pop() method : remove item by keys
car.pop('model')
print(car)

# popitem() method remove the last inserted item
car.popitem()
print(car)

# del keyword : remove the specified key with its value
del car['brand']
print(car)

# del keyword also remove the dictionary completely
del car
# print(car)   # error

# clear() method removes all the elements from the dictionary
car = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
print(car)
car.clear()
print(car)