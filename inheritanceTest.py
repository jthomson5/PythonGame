# Testing inheritance in Python
class Person:       # Class declaration
  def __init__(self, fname, lname, age):
    self.firstname = fname
    self.lastname = lname
    self.age = age

  def sayHello(self):       # Method to say hello
    print(f"Hello my name is {self.firstname} {self.lastname} and I am {self.age} years old!")

x = Person("Jason", "Thomson", 23)
x.sayHello() 

class Student(Person):      # Student inherits Person class
  pass
s1 = Student("Ajax", "Jackson", 21)
s1.sayHello()