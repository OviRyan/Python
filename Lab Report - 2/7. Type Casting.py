import numpy as np

data = np.array([
    ['John', '25', '50000.50'],
    ['Jane', '30', '60000.75'],
    ['Doe', '28', '55000.60']
], dtype='str')

data[:, 1] = data[:, 1].astype(int)  # Convert age column to integers
data[:, 2] = data[:, 2].astype(float)  # Convert salary column to floats

print(data)
