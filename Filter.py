import numpy as np

prices = np.array([15, 25, 40, 60, 45, 30, 80, 35])

# Filter products within the price range of $20 to $50
filtered_prices = prices[(prices >= 20) & (prices <= 50)]
print(f"Filtered prices within $20 to $50: {filtered_prices}")
