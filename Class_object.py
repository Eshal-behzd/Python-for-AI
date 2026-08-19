class car:
    def drive(self):
        print("The car is driving.")
car1 = car()
car1.drive()

class car:
    color = "red"
    def drive(self):
        print(f"The {self.color} car is moving.")
my_car = car()
my_car.drive()

class car:
    color = "blue"
    def drive(self):
        print(f"The {self.color} car is moving.")
    def setcolor(self, new_color):
        self.color = new_color
my_car = car()        
my_car.setcolor("green")
my_car.drive()
