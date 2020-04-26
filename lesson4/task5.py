from functools import reduce

arr = [item for item in range(100, 1001, 2)]
print(arr)
print(reduce(lambda prev_el, el: prev_el * el, arr))
