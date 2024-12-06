# The List 
a = [1, 3, 5, 7, 9]


# Task 1 

print("a[-2]:", a[-2])
print("a[2]:", a[2])
print(f"Length of a: {len(a)}")
print(f"Type of a: {type(a)}")

# Task 2 
a[-3] = 50

print(f"After changing a[3]: {a}")
print(f"a[2:4]: {a[2:4]}")

# Task 3 

a.append(100)
a.insert(2,200)

print(f"After Append & Insert : {a}")

# Task 4

print(f"After Pop : {a.pop()}")
print(f"After Pop Index 1 :  {a.pop(1)}")

# Task 5

x = [2,4,6]
a.extend(x)
print(f"Extening :  {a}")

# Task 6 
b = a.copy()
print(f"Copy To B :  {b}")

# Task 7 
b.sort()
print(f"Sort B :  {b}")

# Task 8 
print("Printing list until 5:")
for lst in a:
    if lst == 5:
        print(lst)
        break
    print(lst)

# Task 9
print(f"Maximum in a :  {max(a)}")

