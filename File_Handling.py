File = open("demo.txt", "r")
# Read and display the contents of the file
print(File.read())
File.close()

# "w" mode will erase the previous content
file = open("demo.txt", "w")
# Write new content to the file
file.write("Its is easy to learn.")
file.close()

# "a" mode adds new content without deleting existing content
file = open("demo.txt", "a")
file.write("\nThis is appended line.")
file.close()

import csv
file = open("Student.csv", "r")
reader = csv.reader(file)
for row in reader:
    print(row)
file.close()

# The with statement automatically closes the file
with open("demo.txt", "r") as file:
    data = file.read()
    print(data)


