import numpy as np

temperatures = np.array([15, 25, 30, 5, 20, 35, 10])

# Find indices where temperature exceeds a certain threshold (e.g., 20)
exceed_threshold_indices = np.where(temperatures > 20)
print(f"Days when temperature exceeds 20°C: {exceed_threshold_indices[0]}")

# Replace temperatures below a threshold (e.g., 10°C) with a minimum value (e.g., 10)
adjusted_temperatures = np.where(temperatures < 10, 10, temperatures)
print(f"Adjusted temperatures (below 10°C replaced with 10°C): {adjusted_temperatures}")
