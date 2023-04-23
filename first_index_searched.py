from sys import argv
from sys import exit


# stock user entry as arguments list
def stock(arg_v):
    arg = arg_v[1:]
    return arg


arguments = stock(argv)


# stock the ultimate word of string as comparative word
def comparative_word_in(arg):
    comparative_word = arg[-1]
    return comparative_word


# take off comparative word from arguments in new argument's list
new_argument_list = arguments[0:len(arguments)-1]


# display -1 if the comparative word is not in string
def is_absent(word):
    if word not in new_argument_list:
        return True
    else:
        return False


def display_error():
    if is_absent(comparative_word_in(arguments)):
        print("-1")
        exit(1)
    else:
        pass


display_error()

# print index off searched word in argument
print(new_argument_list.index(comparative_word_in(arguments)))
