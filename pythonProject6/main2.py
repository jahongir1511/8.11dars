#  https://www.codewars.com/kata/625ea5c1a071210065c923af/train/python

def plastic_balance(lst):
    while len(lst) > 1:
        if lst[0] + lst[-1] == sum(lst[1:-1]):
            return lst
        else:
            lst = lst[1:-1]

    return [] if len(lst) == 1 and lst[0] != 0 else lst


print(plastic_balance([1, 2, 3, 4, 5]))
print(plastic_balance([0, 104, 3, 101, 0, 111]))
print(plastic_balance([1, -1]))
print(plastic_balance([10, 5, -2, 7, -10, 2]))
print(plastic_balance([3, 3, 3, 3, 3, 3]))
print(plastic_balance([0, 0, 0, 0, 0, 0, 0, 0]))
print(plastic_balance([0]))
print(plastic_balance([3]))
