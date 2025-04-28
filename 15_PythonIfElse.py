#### Python If Else ####

#### Python Conditions and If Statements ####
a = 5
b = 6
a == b      # Equal
a != b      # Not Equal
a < b       # Less Than
a <= b      # Less Than Equal
a > b       # Greater Than
a >= b      # Greater Than Equal

# If Statement
if b > a:
    print('b is greater than a1')

# Elif Statement
if b < a:
    pass
elif b > a:
    print('b is greater than a2')
    
# Else Statement
if b < a:
    pass
elif b == a:
    pass
else:
    print('b is greater than a3')

# Short hand if
if b > a: print('b is greater than a4')

# Short hand if else
print("a is greater") if b < a else print("b is greater")

# if else condition with 3 condition
print('A') if a > b else print('=') if a == b else print("B")

# And
a = 2
b = 1
c = 5
if a > b and b < c:
    print('both condition is true')
    
# Or
if a < b or b < c:
    print('second condition is true')

# Not
if not a < b:
    print('a is not less than B')

# Nested If
if a > b:
    if b < c:
        print("a > b < a")
    else:
        print('o')

# The pass Statement
if a > b:
    pass
