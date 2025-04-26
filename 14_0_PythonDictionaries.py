#### Python Dictionaries ####

car = {
    'brand' : 'Ford',
    'model' : 'mustang',
    'year' : 1964
}

print(car)

# Dictionary Items :
print(car["brand"])

# Duplicate not allowed : duplicate value update the previous value
car = {
    'brand' : 'Ford',
    'model' : 'mustang',
    'year' : 1964,
    'year' : 2025
}
print(car)

# Dictionary length
print(len(car))

# Type
print(type(car))

# dic() constructor
car = dict(brand = 'Ford', model = 'mustang', year = 1964)
print(car)