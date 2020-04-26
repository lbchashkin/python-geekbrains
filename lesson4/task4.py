import random

arr = [random.randint(1, 20) for i in range(20)]
print(arr)
arr1 = [el for el in arr if arr.count(el) == 1]
print(arr1)
