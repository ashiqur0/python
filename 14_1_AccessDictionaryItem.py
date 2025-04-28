#### Access Dictionary Item ####

car = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}

print(car['brand'])     # ford

# get() method will provide the same result
print(car.get('brand'))

# Get Keys
# keys() method will return all the key
print(car.keys())

# Get Values
# values() method will return all the value
print(car.values())

# Get Item
# items() method will return all the key and value
print(car.items())