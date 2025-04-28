#### Python Dictionary Method ####

# clear() method : remove all the element from the dictionary
car = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
car.clear()
print(car)      # prints {} empty dictionary

# copy() method : copy a dictionay element to another dictionary
car = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
car2 = car.copy()
print(car2)

# get() method : returns the value of specified key
print(car2.get('brand'))

# keys() method : return a list containing the dictionary's keys
print(car.keys())

# values() method : returns a list containing the dictionary's values
print(car.values())

# items() method : returns a list containg tuple for each key value pair
print(car.items())

# pop() method : Removes the element with the specified keys
car2.pop('brand')
print(car2)

# popitem() method : Removes the last inserted key-value pair
car2.popitem()
print(car2)

# update() method : update the dictionary with the specified key-value pair
car2.update({'model': 'mustang'})
print(car2) 