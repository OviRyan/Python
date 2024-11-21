import numpy as np

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Try reshaping the data to 3 rows and 4 columns
try:
    reshaped_data = data.reshape(3, 4)
    print("Reshaped data (3x4):\n", reshaped_data)
except ValueError as e:
    print(f"Error: {e}")

# If reshaping is not possible, pad/truncate to make it work
desired_size = 3 * 4  # 3 rows * 4 columns
padded_data = np.pad(data, (0, desired_size - len(data)), mode='constant')
reshaped_data = padded_data.reshape(3, 4)

print(f"\nPadded and reshaped data (3x4):\n{reshaped_data}")
