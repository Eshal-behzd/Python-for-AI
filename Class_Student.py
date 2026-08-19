class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def intro(self):
        print(f"My name is {self.name} and I am {self.age} years old.")
student_1 = student("Alice", 20)
student_1.intro()

student_2= student("Bob", 22)
student_2.intro()
