# The Tuple 
a = (1,3,5,7,4)

# Task 1 - Sum of odd numbers
sum = 0  
for x in a:
    if x % 2 != 0:
        sum += x
print(sum)

# Task 2 - Find Sum of All Odd Numbers Indexes

# i didnt understand this task is it sum of indexes or sum of odd numbers in indexes

 

# Task 3 - Count the number of odd and even 
odd_count = sum(1 for num in a if num % 2 != 0)
even_count = sum(1 for num in a if num % 2 == 0)
print(f"Odd count: {odd_count}, Even count: {even_count}")

# Task 4 - Extend the tuple 
extended_tuple = a + (2, 4, 6)
print(f"Extended tuple: {extended_tuple}")

# Task 5 - Add a new item 
modified_tuple = a[:2] + (400,) + a[2:]
print(f"Tuple after adding 400 at index 2: {modified_tuple}")

# Task 6 - Remove the last element 
tuple_without_last = a[:-1]
print(f"Tuple after removing the last element: {tuple_without_last}")

# Task 7 - Perform slicing 
sliced_tuple = a[-4:-1]
print(f"Sliced tuple [-4:-1]: {sliced_tuple}")

# Task 8 -  continue if the value is 5
print("Tuple elements (skipping 5):")
for num in a:
    if num == 5:
        continue
    print(num)
 