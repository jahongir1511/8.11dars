#      https://www.codewars.com/kata/59887207635904314100007b/train/python

def closest(lst):
    closest_value = None
    has_opposite_pair = False

    for num in lst:
        if closest_value is None:
            closest_value = num
        elif abs(num) < abs(closest_value):
            closest_value = num
            has_opposite_pair = False
        elif abs(num) == abs(closest_value):
            if num == 0:
                return 0
            elif num == -closest_value:
                has_opposite_pair = True
            elif num > closest_value:
                closest_value = num
                has_opposite_pair = False

    return None if has_opposite_pair else closest_value


print(closest([2, 4, -1, -3]))
print(closest([5, 2, -2]))
print(closest([5, 2, 2]))
print(closest([13, 0, -6]))
print(closest([-2, 2]))
print(closest([-3, 1, 2, -2]))
print(closest([0, -1, 1]))
print(closest([-1, 1, -1, 1]))
print(closest([0, 0, -1]))
print(closest([1, -2, -3, 3, -1]))
print(closest([-4, 4, -5, 5]))
print(closest([-10, -10, 10]))

