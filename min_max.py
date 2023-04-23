from sys import argv
from sys import exit

# keep user entry as arguments
arguments = argv[1:]


# verify that argument contain just 2 argument
# IF not, return an error an exit the program ELSE, continue
def verify(arg, length):
    if len(arg) == length:
        return True
    else:
        return False


def display_error_in_len():
    if not verify(arguments, 2):
        print("error")
        exit(1)
    else:
        pass


display_error_in_len()


# take argument and print sorted range including them
def range_between(number_one, number_two):
    # sort user entry if is not
    lst = []
    result = ""
    if number_one < number_two:
        lst.append(number_one)
        lst.append(number_two)
    else:
        lst.append(number_two)
        lst.append(number_one)
        number_one = int(lst[0])
        number_two = int(lst[1])
    for i in range(number_one, number_two):
        result += f"{i} "
    return result


print(range_between(arguments[0], arguments[1]))