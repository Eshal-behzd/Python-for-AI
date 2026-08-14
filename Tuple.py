# Tuple: ordered , immutable 
colors = ("green" , "red" , "blue", "red")
print(colors)

# Acessing Tuple 
print(colors[0]) # Accessing the first element
print(colors[-1]) # Accessing the last element

# immutable : Tuples cannot be changed after they are created. You cannot add, remove, or modify elements in a tuple. 
# colors[0] = "yellow"  # This will raise an error because tuples are immutable

# Tuple Methods 

print(colors.count("red"))  # Returns the number of occurrences of the specified element

print(colors.index("red"))
