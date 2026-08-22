# Polymorphism: Different classes have the same method name
class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

for pet in [Dog(), Cat()]:
    pet.speak()

# Method Overriding: Child class redefines the parent's method
class Vehicle:
    def move(self):
        print("Vehicle is moving!")

class Car(Vehicle):
    def move(self):
        print("Car is driving!")
car = Car()
car.move()

# Default Arguments: A method can work with different numbers of argument
class Calculator:
    def add (self, a, b=0, c=0):
        return a + b + c
cal = Calculator()
# Only a is provided; b and c use their default value 0
print(cal.add(5))
# a and b are provided; c uses its default value 0
print(cal.add(3, 6))
# All three arguments are provided
print(cal.add(2, 5, 1)) 
