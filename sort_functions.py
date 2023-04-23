"""SORTING NUMBERS"""

# ASCENDING SORT
def get_more_less_number_from(array):
    result = array[0]
    for number in array:
        if number < result:
            result = number
        else:
            result = result
    return result

def sort_in_ascending_order(array):
    result = [0] * len(array)
    for i in range(len(array)):
        result[i] = get_more_less_number_from(array)
        array.remove(result[i])
    return result

# DESCENDING SORT
def get_more_large_number_in(lst):
    more_large_number = 0
    for i in range(len(lst)):
        if lst[i] > more_large_number:
            more_large_number = lst[i]
        else:
            continue

    return more_large_number
def sort_in_descending_order(lst):
    result = [0] * len(lst)
    for i in range(len(lst)):
        result[i] = get_more_large_number_in(lst)
        lst.remove(result[i])
    return result

"""SORTING LETTERS BY ASCII"""
# ASCENDING
# DESCENDING

