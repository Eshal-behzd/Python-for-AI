class student:
    def __init__(self, name, grade):
        self.name = name    # public attribute
        self.__grade = grade   #private attribute
 # To access private attribute 
    def get_grade(self):
        return self.__grade 

student1 = student("Ali", 90)
print(student1.name)
# print(student1.grade)   #Error 
print(student1.get_grade())


class student:

    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade

    def get_grade(self):
        return self.__grade
    
    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else :
            print("Invalid grade")

student2 = student("Bob", 90)
student2.set_grade(80)
print(student2.get_grade())

