# Testing out Python Classes and Objects
class testClass:        # Simple class
    x = 25
o1 = testClass()        # Object of class
print(o1.x)
# init function
class Student:
    def __init__(self, name, gpa, year):        # Init class
        self.name = name
        self.gpa = gpa
        self.year = year

    def __str__(self):      # Allows object to be printed
        return f"Student name: {self.name} Student GPA: {self.gpa} Student year: {self.year}"

    def greetFunc(self):    # Define function in class
        print(f"Hello my name is {self.name}, and I am a {self.year} with a GPA of {self.gpa}")

s1 = Student("Jason", 3.7, "Senior")            # Init student
print(f"Student name: {s1.name} Student GPA: {s1.gpa} Student year: {s1.year}")      # Can print like this
print(s1)       # Can print like this with __str__ function
s1.greetFunc()
# Change object properties
s1.gpa = 4.0
print(s1.gpa)
del s1.gpa
print(s1.gpa)       # Error