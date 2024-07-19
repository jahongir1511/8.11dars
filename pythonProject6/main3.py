#   https://www.codewars.com/kata/5729c30961cecadc4f001878/train/python


def unite_unique(*arrays):
    unique_elements = set()
    result = []

    for array in arrays:
        for item in array:
            if item not in unique_elements:
                unique_elements.add(item)
                result.append(item)

    return result


print(unite_unique([1, 2, 3], [2, 3, 4]))
print(unite_unique([1, 2], [2, 3], [3, 4]))
print(unite_unique([1, 1, 1], [2, 2, 2], [3, 3, 3]))
print(unite_unique([5, 6], [7, 8], [5, 9]))
print(unite_unique([], [1, 2], [2, 3]))


