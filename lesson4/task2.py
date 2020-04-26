import random

arr1 = [random.randint(1, 1000) for i in range(15)]
print(arr1)
arr2 = [arr1[i] for i in range(1, len(arr1)) if arr1[i] > arr1[i - 1]]
print(arr2)
