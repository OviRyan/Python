import numpy as np

sales_data = np.array([
    [100, 150, 200, 250],
    [120, 180, 240, 300],
    [110, 170, 220, 270],
    [130, 190, 250, 310]
])

print(sales_data[:3])  # First three products
print(sales_data[:, -2:])  # Last two months
print(sales_data[1, 3])  # 2nd product in 4th month
