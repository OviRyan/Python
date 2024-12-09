import numpy as np

branch1_sales = np.array([100, 200, 300])
branch2_sales = np.array([150, 250, 350])

# Horizontal Join (along columns)
horizontal_join = np.column_stack((branch1_sales, branch2_sales))
print(f"Horizontal Join (Columns - Two Branches):\n{horizontal_join}")

# Vertical Join (along rows)
vertical_join = np.vstack((branch1_sales, branch2_sales))
print(f"\nVertical Join (Rows - Two Branches):\n{vertical_join}")
