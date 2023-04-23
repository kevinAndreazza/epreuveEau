import sys
import my_functions

arguments = my_functions.get_arguments(sys.argv)

my_functions.verify_len(arguments, 2)


def bubble_sort(array):
    index_letter = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[j][index_letter] < array[i][index_letter]:
                array[j], array[i] = array[i], array[j]
            else:
                array[j], array[i] = array[j], array[i]
    return array

sorted_array = bubble_sort(arguments)

print(arguments)