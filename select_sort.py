from sys import argv
from sys import exit

""" FUNCTIONS """

# for save user_entry
def stock(user_entry):
    result = user_entry[1:]
    return result
user_input = stock(argv)

# make sure that items on list are integer
def integer(lst):
    result = []
    for x in lst:
        x = int(x)
        result.append(x)
    return result
user_input = integer(user_input)


# for catch errors
def verify(user_entry, length):
    if len(user_entry) < length:
        return False
    else:
        return True

def is_alpha(user_entry):
    for x in user_entry:
        try:
            if int(x):
                return True
            else:
                return False
        except ValueError:
            continue

def is_not_alpha(user_entry):
    for x in user_entry:
        try:
            if str(x) != int(x):
                return True
            else:
                return False
        except ValueError:
            continue


# Display error's caught
def display_error():
    if verify(user_input, 2):
        pass
    else:
        print("error")
        exit(1)

    if is_alpha(user_input):
        pass
    else:
        print("error")
        exit(1)

    if is_not_alpha(user_input):
        pass
    else:
        print("error")
        exit(1)
display_error()


"""SOLVING PROBLEM"""
def get_more_less_number_from(array):
    result = array[0]
    for number in array:
        if number < result:
            result = number
        else:
            result = result
    return result


def extraction_sort(array):
    result = [0] * len(array)
    for i in range(len(array)):
        result[i] = get_more_less_number_from(array)
        array.remove(result[i])
    return result
sorted_array = extraction_sort(user_input)

"""OUTPUT"""

# transform the result
def make_string_for_output(array):
    result = ""
    for number in array:
        result += f"{number} "
    return result

# save the result as output and print it
output = make_string_for_output(sorted_array)
print(output)