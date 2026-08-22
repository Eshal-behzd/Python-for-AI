# Create a custom exception class for invalid ages
class invalidAgeError(Exception):
    pass

try :
    age= int(input("Enter your age:"))
    if age < 0:
    # Raise the custom exception if the age is negative    
        raise invalidAgeError(f"Age can't be negative!, {age}")
except invalidAgeError as e :
    print(e)
