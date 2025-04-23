################ Python Operators ################

#### Arithmetic Operators ####
x = 4
y = 2

a = x + y   # Addition
b = x - y   # Subtraction
c = x * y   # Multiplication
d = x / y   # Division
e = x % y   # Modulus
f = x ** y  # Exponentiation
g = x // y  # Floor division


#### Assignment Operator ####
x = y
x += y
x -= y
x *= y
x /= y
x %= y
x **= y
x //= y
# x &= y
# x |= y
# x ^= y
# x >>= y
# x <<= y
print(x := y)


# Python Comparison Operator
x == y
x != y
x > y
x < y
x >= y
x <= y


# Python Logical operator
x = y = 3
if x > 0 and x < 5 or y > 0 and y < 5:
    if not x != y:
        print("Hello")


# Python Identity Operator
x = 4
y = 5
z = x
print(x is z)       # Returns True if both variables are the same object
print(x is not y)


# Python Membership Operator: Membership operators are used to test if a sequence is presented in an object
fruits = ["apple", "banana", "cheryy"]
if "apple" in fruits:
    print('Yes')

if "mango" not in fruits:
    print("No")
    
#### Python Bitwise Operator ####
print(6 & 3)    # Bitwise AND           # 2
print(6 | 3)    # Bitwise OR            # 7
print(6 ^ 3)    # Bitwise XOR           # 5
print(~3)       # NOT (Inverse all bit) # -4
print(3 << 2)   # Zero fill Left Shift  # 12
print(8 >> 2)   # Sign Right shift      # 2

# Operator Precedence
