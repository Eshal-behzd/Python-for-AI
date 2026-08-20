class Dog :
    def __init__(self):
        self.name ="Buddy"
    def bark(self):
        print(f"{self.name} says WOOF!")    
dog_1 = Dog()
dog_1.bark()

class car :
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
car1 = car("Toyota" , "White")
print(car1.brand)
print(car1.color)
car2 = car("Honda" , "Red")
print(car2.brand)
print(car2.color)
car1.color = "blue"    # Color of car1 will change 
print(car1.color)        
