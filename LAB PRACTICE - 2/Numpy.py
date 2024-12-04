import numpy as np

def analyze_scores(scores):
    # Calculate the average score per student
    averages = np.mean(scores, axis=1)
    
    # Find the student with the highest average
    highest_avg_index = np.argmax(averages)
    highest_avg_score = averages[highest_avg_index]
    
    print(f"Highest Average: {highest_avg_score}, Student Index: {highest_avg_index}")

# Example usage
scores = np.array([
    [85, 90, 78],  # Student 0
    [88, 92, 95],  # Student 1
    [70, 65, 80]   # Student 2
])

analyze_scores(scores)