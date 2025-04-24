#### Loop List ####
# Loop through a list
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)

# Loop through the index number
for x in range(len(fruits)):
    print(fruits[x])

# Using While Loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# Looping using list comprehension
[print(x) for x in fruits]

