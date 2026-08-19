class car :
    def __init__(self, color):
        self.color = color 
    def start(self):
        print(f"The {self.color} car has started.")

#First car object
car_1 = car("red")
car_1.start()

# Second car object
car_2 = car("blue")
car_2.start()
