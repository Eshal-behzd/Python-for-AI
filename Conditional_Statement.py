# elif Statement
score = int(input("Enter your score : "))
if(score > 90):
    print("A")
elif(score > 80):
    print("B")
else :
    print("Try Again")        

# Nested if Statement
age = int(input("Enter your age : "))
country = input("Enter your country : ").capitalize()
if age >= 18:
    if country == "Pakistan":
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")
else:
    print("You are not eligible to vote")            

# Combine Conditional Statements
age = int(input("Enter your age : "))
country = input("Enter your country : ").capitalize()
if age >= 18 and country == "Pakistan":
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")         

#multiple conditions
marks = 70
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Grade F")
 