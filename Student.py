class Student:
    # constructor method
    def __init__(self, name, age, grade):
        self.name = name    #instance variable
        self.age = age
        self.grade = grade
    def display_info(self):
        print(f"Student Name: {self.name}") 
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")
        
    
    def is_eligible(self):
        if self.age >= 15 :
            print(f"{self.name} is eligible for Admission.")  
        else:
            print(f"{self.name} is not eligible for Admission.")    
# creating objects
student1 = Student("Bob" , 23 , "A")
# accessing attributes
print(student1.name)
print(student1.age)

# calling method

student1.display_info()
student1.is_eligible()



