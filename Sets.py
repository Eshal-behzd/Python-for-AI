# Sets: unordered collection of unique elements
# Sets are mutable, meaning you can add or remove elements from a set after it is created
# Sets do not allow duplicate elements.

my_set = {1, 2, 3, 4, 4, 5}
print("my_set:", my_set)

# Set Method
my_set.add(6)  
print("after add:", my_set)

my_set.remove(3)  # Removes the specified element from the set
print("after remove:", my_set)

# Set Operation 
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
