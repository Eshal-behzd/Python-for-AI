student = {
    "name" : "Ali",
    "age" : 24,
    "grade" : "A"
}
# print key only
for key in student:
    print("key:", key)

# print key value
for key in student:
    print("Key value: " , student[key])

# print key-value pairs
for key in student:
    print(key ,":", student[key])

student_list =[
    {
    "name" : "Ali",
    "age" : 24,
    "grade" : "A"
    },
    {
    "name" : "sara",
    "age" : 19,
    "grade" : "A"
    }
]
for student in student_list:
    print(f"Name: {student.get('name' , '' )} | Grade: {student.get('grade' , '')}")
