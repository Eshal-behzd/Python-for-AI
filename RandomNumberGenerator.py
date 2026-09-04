import numpy as np
# seed is used to initialize the random number generator for reproducibility
rng = np.random.default_rng(seed=42)  
flip = rng.choice([True, False], size=10)  # Generate an array of 10 random boolean values
print(flip)  # Print the generated boolean array
prob_heads = np.mean(flip)  # Calculate the mean of the boolean array (proportion of True values)
print(f"Probability of heads: {prob_heads}")

rng = np.random.default_rng()
flip = rng.integers(0, 2, size=10)
print (flip)  # Print the generated array of random integers (0 or 1)
prob_heads = np.mean(flip)  # Calculate the mean of the integer array (proportion of 1s)
print(f"Probability of heads: {prob_heads}")    

import time 
start = time.time()  # Record the start time
sq = [i**2 for i in range(1000000)]  # Create a list of squares using a list comprehension
end = time.time()  # Record the end time
print(f"Loop time: {end - start} seconds")  # Print the time taken

start = time.time()  # Record the start time
sq = np.arange(1000000)**2  # Create an array of squares using NumPy's arange function
end = time.time()  # Record the end time    
print(f"Vectorized time: {end - start} seconds")  # Print the time taken