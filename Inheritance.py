class Animal:
    def speak(self):
        print("Some sound!")

class Dog(Animal):
    pass
dog = Dog()
dog.speak()

class Cat(Animal):
    def sound(self):
        print("Meow!")
cat = Cat()
cat.sound()
cat.speak()

# Method Overriding
class Cow(Animal):
    def speak(self):
        print("MOOO!")
cow = Cow()
cow.speak()
