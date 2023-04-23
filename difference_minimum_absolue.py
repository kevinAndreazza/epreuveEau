from sys import argv
from sys import exit
from mesFonctions import sort_in_descending_order

# stock argv in argument's list
arguments_list = argv[1:]


# verify that argument contain just 2 argument
# IF not, return an error an exit the program ELSE, continue
def verify(arg, length):
    if len(arg) >= length:
        return True
    else:
        return False


def display_error_in_len():
    if not verify(arguments_list, 2):
        print("error")
        exit(1)
    else:
        pass


display_error_in_len()


# if letter in string this is true, else is false
def is_letter(lst):
    for letter in lst:
        try:
            if int(letter):
                return True
            else:
                return False
        except ValueError:
            if str(letter):
                return False
            else:
                return True


def display_error_int(lst):
    if not is_letter(lst):
        print("error")
        exit(1)
    else:
        pass


display_error_int(arguments_list)


# transform each argument as integer
def get_int_from(lst):
    result = []
    for n in lst:
        n = int(n)
        result.append(n)
    return result


arguments = get_int_from(arguments_list)

# sort numbers in descending order
arguments = sort_in_descending_order(arguments)


# save result of all subtractions

def subtract_elements_of(lst):
    results = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            result = lst[i] - lst[j]
            print(result)
            results.append(result)
        return results


subtract_elements = subtract_elements_of(arguments)

absolute_minimal_difference = sort_in_descending_order(subtract_elements)
output = absolute_minimal_difference[-1]
print(output)

