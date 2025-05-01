#### Python Class Object ####

# Create a class
class Student:
    name = 'John'

# Create Object
obj = Student
print(obj.name)

# __init__() function :
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Rahim', 20)
print('Name: ' + p1.name)
print('Age:', p1.age)

# The __str__() function
class Student2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} {self.age}"
        
s1 = Student2("Joy", 20)
print(s1)

# Object Method : Object can alson contains methods
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfun(self):
        print("Hello, I'm " + self.name)
        
p1 = Person2("John", 30)
p1.myfun()

# The self Parameter : we can use any variable name, but it should be the first parameter
class Person3:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    
    def __str__(mysillyobject):
        return f"{mysillyobject.name} {mysillyobject.age}"

p = Person3('John', 36)
print(p)

# Modify object properties
p.age = 40
print(p)

# Delete Object Properties : Delete the age property from p object
del p.age
# print(p)

# Delete Object
del p

# The pass Statement
class MyClass:
    pass