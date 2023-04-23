from sys import argv
from sys import exit


# errors
if len(argv) != 3:
    print("error")
    exit(1)


# variables
arg_as_ref = argv[1]
arg_ask_to_ref = argv[2]


# errors
try:
    arg_as_ref = int(arg_as_ref)
    arg_ask_to_ref = int(arg_ask_to_ref)
    if arg_as_ref == int(arg_as_ref):
        print("error")
        exit(1)
    if arg_ask_to_ref == int(arg_ask_to_ref):
        print("error")
        exit(1)
except ValueError:
    pass


# functions
def string_in_string(x, y):
    if y in x:
        print("true")
    if y not in x:
        print("false")


string_in_string(arg_as_ref, arg_ask_to_ref)