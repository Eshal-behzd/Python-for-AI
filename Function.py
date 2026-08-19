def greet():
    print("Hello World!")
# call the function 
greet()

# function with parameter
def greet(name):
    print("Hello, " + name + "!")
greet("John")

greet("Alice")

# returning values from a function
def add(a , b ):
    return a + b
result = add(2 , 3)
print (result)

def square(num):
    return num* num

ans = square(5 )
print(ans)