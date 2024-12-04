import numpy as np

scores = np.array([85, 75, 90, 60, 95, 80])

# Search for specific scores and return their indices
indices_75 = np.where(scores == 75)[0]
indices_90 = np.where(scores == 90)[0]
print(f"Indices of score 75: {indices_75}")
print(f"Indices of score 90: {indices_90}")

# Sort the array in ascending order
sorted_ascending = np.sort(scores)
print(f"Scores sorted in ascending order: {sorted_ascending}")

# Sort the array in descending order
sorted_descending = np.sort(scores)[::-1]
print(f"Scores sorted in descending order: {sorted_descending}")
