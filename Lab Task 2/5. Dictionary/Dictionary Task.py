employee = {
    "name": "A",
    "age": 40,
    "type": {"developer": ["iOS", "android"]},
    "permanent": True,
    "salary": 30000,
    100: (1, 2, 3),
    4.5: {5, 6, "Tone", 7, 1}
}
# Task 1 
print("Length of employee: ", len(employee))
print("Type of employee: ", type(employee))

# Task 2

print("Accessing the developer key:", employee["type"]["developer"])