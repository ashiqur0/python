#### Python Functions ####

# Creating a Function
def fun():
    print('Hello')

# Calling a Function
def fun2():
    print('Hello2')

fun2()

# Parameter and Arguments
def fun3(name):
    print('Hello, ' + name)

x = 'Rabbi'
fun3(x)

# Argument: The variable that is pass a vlue to the calling function, is called Argument.

# Parameter: The variable that receive a value in function definition, is called parameter.

#### Number of Arguments ####
def fun4(fname, lname):
    print('Hello, ' + fname + ' ' + lname)

fun4('Rabbi', 'Hassan')

# Arbitary Argumets *args
def fun5(*fruits):
    print(fruits[0])

fun5('apple', 'banan', 'cherry')

# Keyword Argument : order do not need to main tain
def fun6(fruits3, fruits2, fruits1):
    print(fruits1 + " " + fruits2 + " " + fruits3)

fun6(fruits1='apple', fruits2='banana', fruits3='cherry')

# Arbitarry Keyword Argument
def fun7(**args):
    print('His last name is: ' + args['lname'])

fun7(fname='Rabbi', lname='Hassan')

# Default Parameter Value
def fun8(country = 'Norway'):
    print("I'm from " + country)

fun8('India')
fun8('Pakistan')
fun8()      # If we do not pass any argument, it will print the default value
fun8('Bangladesh')

# Passing a list as argumet
def fun9(fruits):
    for x in fruits:
        print(x)

fruits = ['apple', 'banana', 'cherry']
fun9(fruits)

# Return Values
def fun10(num):
    return num * num
print(fun10(1))
print(fun10(2))
print(fun10(3))
print(fun10(4))
print(fun10(5))

# The pass Statement
def fun11():
    pass

# Positional only Arguments
def fun12(x, /):
    print(x)
fun12(3)

# Keyword only Arguments
def fun13(*,x):
    print(x)
fun13(x=2)

# Combine positional only and Keyword only
def fun14(a, b, /, *, c=3, d=4):
    print(a + b + c + d)

fun14(2, 3, c=3, d=4)

# Recursion : Find nth position Fibonacci Number
def fun15(n):
    if n <= 1:
        return n
    else:
        return fun15(n-1) + fun15(n-2)
    
print(fun15(6))