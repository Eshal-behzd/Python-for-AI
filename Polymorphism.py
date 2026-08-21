class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

for pet in [Dog(), Cat()]:
    pet.speak()


class Vehicle:
    def move(self):
        print("Vehicle is moving!")

class Car(Vehicle):
    def move(self):
        print("Car is driving!")
car = Car()
car.move()

class Calculator:
    def add (self, a, b=0, c=0):
        return a + b + c
cal = Calculator()
print(cal.add(5))
print(cal.add(3, 6))
print(cal.add(2, 5, 1)) 
