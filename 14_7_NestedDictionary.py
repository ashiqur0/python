#### Nested Dictioanry ####

# Create a Dictioanry that contain three dictionary
student = {
    'student1' : {
        'name': 'samiul',
        'roll': 1
    },
    'student2': {
        'name': 'ripa',
        'roll': 2
    },
    'student3': {
        'name': 'ruhi',
        'roll': 3
    }
}
print(student)

# Create three dictionary, then create one dictionary that contains other three dictionary
student1 = {
    'name': 'samiul',
    'roll': 1
}
student2 = {
    'name': 'ripa',
    'roll': 2
}
student3 = {
    'name': 'simanto',
    'roll': 3
}
student02 = {
    'studen1' : student1,
    'student2': student2,
    'student3': student3
}

# Access Item in Nested Dictionary
print(student02['studen1']['name'])

# Loop Through Nested Dictionary
for x, obj in student02.items(): 
    print(x)
    for y in obj:
        print(y + ':' + str(obj[y]))