#### Python While Loop ####

i = 1
while i < 5:
    print(i)
    i += 1

# The break Statement
i = 1
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

# The continue Statement
i = 1
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

# The else Statement
else: 
    print('i is no longer less than 10')