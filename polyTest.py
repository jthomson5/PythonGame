# Testing polymorphism in Python
class Animal:       # Parent Class
    def __init__(self, color, size):
        self.color = color
        self.size = size
    def speak(self):
        pass
class Dog(Animal):  # Inherited Animal with different speak method
    def __init__(self, color, size):
        super().__init__(color, size)
    def speak(self):
        print("Woof!")
class Lion(Animal):     # Inherited Animal with different speak method
    def __init__(self, color, size):
        super().__init__(color, size)
    def speak(self):
        print("ROAR!")
animals = [Dog("Brown and White", "Small"), Lion("Yellow-Gold", "Large")]
for animal in animals:
    animal.speak()