import numpy as np

# Axis Concept in NumPy

# In a 2D NumPy array, axis tells us the direction
# along which an operation should be performed.

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Original Array:")
print(arr)


# axis = 0
# axis=0 means the operation is performed vertically.
# It works down the rows and gives a result for each column.

print("\nSum using axis=0:")
print(np.sum(arr, axis=0))

# Output: [50 70 90]
# 10 + 40 = 50
# 20 + 50 = 70
# 30 + 60 = 90


# axis = 1
# axis=1 means the operation is performed horizontally.
# It works across the columns and gives a result for each row.

print("\nSum using axis=1:")
print(np.sum(arr, axis=1))

# Output: [60 150]
# 10 + 20 + 30 = 60
# 40 + 50 + 60 = 150


# Example with mean

print("\nMean using axis=0:")
print(np.mean(arr, axis=0))

print("\nMean using axis=1:")
print(np.mean(arr, axis=1))
