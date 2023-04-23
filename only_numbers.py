from sys import argv
from mesFonctions import *


# save user entry as argument
argument = argv[1:]


# take argument and make string with it
def get_string(arg):
    result = ""

    for word in argument:
        if word == arg[len(arg) - 1]:
            result += f"{word}"
        else:
            result += f"{word} "
        result = result

    return result


string = get_string(argument)


# spot if it's letter in string
# if letter in string the is false, else is true
def is_letter(strings):
    for letter in strings:
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


print(is_letter(string))