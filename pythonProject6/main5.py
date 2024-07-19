#   https://www.codewars.com/kata/5b5e0ef007a26632c400002a/train/python

def elements_sum(arrays, default=0):
    total_sum = 0
    n = len(arrays)

    for i in range(n):
        sub_array = arrays[i]
        position = n - i - 1
        if position < len(sub_array):
            total_sum += sub_array[position]
        else:
            total_sum += default

    return total_sum


# Test cases
print(elements_sum([[3, 2, 1, 0], [4, 6, 5, 3, 2], [9, 8, 7, 4]]))
print(elements_sum([[1], [2, 3], [4, 5, 6]], default=10))
print(elements_sum([[1, 2], [3, 4], [5, 6, 7]], default=0))
print(elements_sum([[1, 2], [3, 4, 5], [6]], default=0))
print(elements_sum([[1, 2], [3, 4], [5, 6, 7]], default=1))  
