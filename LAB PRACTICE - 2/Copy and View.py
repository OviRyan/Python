import numpy as np

data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

row_view = data[1, :]  # View of the second row
col_copy = data[:, 2].copy()  # Deep copy of the third column

row_view[0] = 100  # Modify the row view
col_copy[0] = 200  # Modify the column copy

print(f"Row View modified: {row_view}")
print(f"Column Copy modified: {col_copy}")
print(f"Original Data after modifications:\n{data}")
