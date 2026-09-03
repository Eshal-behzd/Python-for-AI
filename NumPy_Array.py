import numpy as np
arr = np.array([
    [1, 20, 3],
    [4, 43, 5],
    [46, 56, 62]
])

# Accessing elements
print(arr[0, 0])  
print(arr[0, 2])
print(arr[-1, -1])
print(arr[-3, -3])

# General form : arr[row_start:row_end, col_start:col_end]
print(arr[0:2, 1:3])

print(arr[::2, ::2])  # Every second row and column

slice_arr = arr[0, :2]
slice_arr[0] = 100  # Modifying the slice will affect the original array
print(arr[0])

copy_arr = arr[0, :2].copy()
copy_arr[1] = 200  # Modifying the copy will not affect the original
print(arr[1])

