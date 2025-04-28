#### Loop Dictionaries ####

car = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}

# Print All The Keys
for x in car.keys():
    print(x)
    
for x in car:
    print(x)
    
# Print All The Values
for x in car.values(): 
    print(x)

for x in car:
    print(car[x])
    
# Item
for x in car.items():
    print(x)