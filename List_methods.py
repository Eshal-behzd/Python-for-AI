# List : ordered, mutable, allows duplicate elements

fruits = ['apple', 'banana', 'cherry', 'orange', 'banana']
print("fruits:", fruits)

# Accessing elements in a list using indexing. Lists are zero-indexed, meaning the first element is at index 0.
first_fruit = fruits[0]  # Accessing the first element
print("first_fruit:", first_fruit)

# Accessing elements from the end of the list using negative indexing.
last_fruit = fruits[-1]  # Accessing the last element
print("last_fruit:", last_fruit)

# Slicing a list to access a range of elements.
sublist = fruits[1:4]  # Accessing elements from index 1 to 3
print("sublist:", sublist)

# Methods :
fruits.append("kiwi")  # Adds an element to the end of the list
print("after append:", fruits)

fruits.remove("banana")  # Removes the first occurrence of the specified element
print("after remove:", fruits)

fruits.sort()  # Sorts the list in ascending order
print("after sort:", fruits)

fruits.reverse()  # Reverses the order of the list
print("after reverse:", fruits)

fruits.insert(1, "mango")  # Inserts an element at the specified index
print("after insert:", fruits)

fruits.pop()  # Removes and returns the last element of the list
print("after pop:", fruits)

fruits.extend(["grape", "pear", "peach"])  # Extends the list by appending elements from another iterable
print("after extend:", fruits)

# Returns the number of occurrences of the specified element
print("banana count:", fruits.count("banana"))

fruits.clear()  # Removes all elements from the list
print("after clear:", fruits)

# looping through list 
names = ['Alice', 'Bob', 'Charlie', 'David']
for name in names:
    print("Name:", name)
