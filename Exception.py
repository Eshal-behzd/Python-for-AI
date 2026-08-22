try:
    num = int(input("Enter a number: "))
    print(10 / num)

# Handle the error if the user enters 0    
except ZeroDivisionError:
    print("You can't divide num by 0.")
# Handle the error if the input is not a valid integer    
except ValueError:
    print("That's not a number.")
# Handle any other unexpected error    
except Exception as e:
    print(f"An unexpected error occured: {e}")            

# Try to run some code
try:
    print("Running Code....")
# Handle any error that occurs    
except:
    print("Error Found!")

# Run this block if no error occurs    
else:
    print("No Error Found!")

# This block always runs, whether an error occurs or not    
finally:
    print("Done!")

# Raising Exception
age = -3
if age < 0:
# Raise an error because age cannot be negative
    raise ValueError("Age can not be negative!")

