import numpy as np

# Sample 3D array (3 devices, 2 days, 4 data points per day)
data = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]],
                 [[9, 10, 11, 12], [13, 14, 15, 16]],
                 [[17, 18, 19, 20], [21, 22, 23, 24]]])

# Flatten the 3D array into a 1D array
flattened_data = data.flatten()

print(f"Flattened Data: {flattened_data}")
