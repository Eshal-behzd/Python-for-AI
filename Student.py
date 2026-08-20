class Student:
    def __init__(self, name, age, grade):
        self.name = name 
        self.age = age
        self.grade = grade
    def display_info(self):
        print(f"Student Name: {self.name}") 
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")
        
    
    def is_eligible(self):
        if self.age >= 15 :
            print(f"{self.name} is eligilbe for Admission.")  
        else:
            print(f"{self.name} is not eligilbe for Admission.")    

student1 = Student("Bob" , 23 , "A")

print(student1.name)
print(student1.age)
print(student1.grade)
student1.is_eligible()



