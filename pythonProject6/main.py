#         https://www.codewars.com/kata/53da6a7e112bd15cbc000012/train/python

def sort_dict(d):
    sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return sorted_items

