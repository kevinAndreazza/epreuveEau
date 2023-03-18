from sys import argv
from sys import exit

arg = argv[len(argv)::-1]
arg = arg[0: -1]

def int_in_string_detection(x):
    phrase = ""
    for word in x:
        words = f"{word}"
        phrase += f"{words} "

    for char in phrase:
        for n in range(10):
            if char == f"{n}":
                resultat = False
            else:
                resultat = True

            if not resultat:
                print("/!\\ Error! You had to wrote a string of characters.")
                exit(1)
    for word in x:
        print(word)

int_in_string_detection(arg)