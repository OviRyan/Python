a = [12,10,20,-45]
b = [23,47,29,99]

def merge_array(array1,array2):
     return set(array1 + array2)

c = merge_array(a,b)
print(c)
print(sorted(c))