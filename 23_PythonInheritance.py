#### Python Inheritance ####

# Create a Parent Class
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname =  lastname
    
    def printname(self):
        print(self.firstname, self.lastname)
    
p1 = Person("John", "Doe")
p1.printname()

# Create a Child class
class Student(Person):
    pass
s = Student("Doe", "John")
s.printname()

# Add __init__() function
class Student2(Person):
    def __init__(self, firstname, lastname):
        Person.__init__(self, firstname, lastname)
        
x = Student2("Mike", "Mike")
x.printname()

# Add the super() Function
class Student3(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)

x = Student3("Peter", "Perkar")
x.printname()

# Add Properties
class Student4(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
        self.graduateyear = 2027

x = Student4("Jenny", "Ora")
print(x.graduateyear)

# Add parameter
class Student5(Person):
    def __init__(self, firstname, lastname, year):
        super().__init__(firstname, lastname)
        self.year = year
        
x = Student5("Ashiqur", "Rahman", 2026)
print(x.year)

# Add Methods
class Student6(Person):
    def __init__(self, firstname, lastname, year):
        super().__init__(firstname, lastname)
        self.year = year
        
    def newfunction(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.year)

x = Student6("Sabit", "Rahman", 2027)
x.newfunction()

# 