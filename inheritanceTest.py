# Testing inheritance in Python
class Person:       # Class declaration
  def __init__(self, fname, lname, age):
    self.firstname = fname
    self.lastname = lname
    self.age = age

  def sayHello(self):       # Method to say hello
    print(f"Hello my name is {self.firstname} {self.lastname} and I am {self.age} years old!")

  def sayHi(self):
    print("Hiiii!!!")

x = Person("Jason", "Thomson", 23)
x.sayHello() 

class Student(Person):      # Student inherits Person class
  def __init__(self, fname, lname, age, gpa, year):
    self.gpa = gpa    # Add custom attributes
    self.year = year
    super().__init__(fname, lname, age)   # Keep person attributes and methods

  def studentHello(self):   # Define student specific hello
    print(f"Hello my name is {self.firstname} {self.lastname} and I am {self.age} years old! I am a {self.year} with a GPA of {self.gpa}")

s1 = Student("Ajax", "Jackson", 21, 3.9, "Junior")   # Can use Person attributes with the student class
s1.sayHello()
s1.studentHello()

