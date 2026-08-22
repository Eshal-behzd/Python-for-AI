# Error
# with open("missing.txt", "r") as file:
#     print(file.read())

# Try to open a file that does not exist
try:
    with open("missing.txt", "r") as file:
        print(file.read())

# Handle the error if the file is not found
except FileNotFoundError:
    print("File not found!")

filename = "my_info.txt"
Name = "Bob"
Age = 19
Marks = 89
try:
    with open("filename", "r") as fin:
        print(fin.read())
except FileNotFoundError:

# If the file does not exist, create it    
    with open(filename, "w") as fout:
        fout.write(f"{Name}\n {Age}\n {Marks}")

# Open the newly created file and read its contents        
    with open(filename, "r")as fin:
        print(fin.read())
            

