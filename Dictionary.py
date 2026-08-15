# Dictionary: unordered collection of key-value pairs
Student = {
    "name": "John",
    "age": 20,
    "course": "Computer Science"
}
print("Student:", Student)

# Accessing values in a dictionary using keys
print(Student["name"])
print(Student.get("age"))

# Methods

# Adding a new key-value pair to the dictionary
Student["city"] = "New York"
print(Student)

# updating an existing key-value pair in the dictionary
Student["course"] = "Data Science"
print(Student)

# Removing a key-value pair from the dictionary 
Student.pop("course")
print(Student)

# loops through dictionary
for key,value in Student.items():
    print(key, ":", value)
