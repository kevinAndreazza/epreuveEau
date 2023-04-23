# import module from system
from sys import argv
from sys import exit

# save user entry as argument
argument = argv[1:]


# display an error if argument contain number
def display_error_in(arg):
    for word in arg:
        for character in word:
            try:
                if int(character):
                    print("error")
                    exit(1)
                else:
                    pass
            except ValueError:
                pass


display_error_in(argument)


# display an error if it's a special character
def display_error_special_char(arg):
    special_character = []

    for i in range(ord("!"), ord("/")):
        special_character.append(chr(i))
    for i in range(ord(":"), ord("@")):
        special_character.append(chr(i))
    for i in range(ord("["), ord("`")):
        special_character.append(chr(i))
    for i in range(ord("{"), ord("~")):
        special_character.append(chr(i))
    special_character = special_character

    for word in arg:
        for letter in word:
            if letter in special_character:
                print("error")
                exit(1)


display_error_special_char(argument)


# get argument as string of character
def get_string(arg):
    result = ""

    for word in arg:
        if word == arg[len(arg)-1]:
            result += f"{word}"
        else:
            result += f"{word} "

    return result


string = get_string(argument)


# create a function that spot a character and detect if it's lower or uppercase letter
def is_upper(letter):
    if ord("A") <= ord(letter) <= (ord("Z")) or ord("À") <= ord(letter) <= ord("Ý"):
        return True
    else:
        return False


def is_lower(letter):
    if ord("a") <= ord(letter) <= ord("z") or ord("à") <= ord(letter) <= ord("ÿ"):
        return True
    else:
        return False


def is_space(letter):
    if letter == " ":
        return True
    else:
        return False


# create a function that get lower to upper and upper to lower
def get_lower(letter):
    if is_upper(letter):
        lower_letter = chr(ord(letter) + 32)
        return lower_letter
    else:
        return letter


def get_upper(letter):
    if is_lower(letter):
        upper_letter = chr(ord(letter) - 32)
        return upper_letter
    else:
        return letter


def get_space(character):
    if ord(character) == 32:
        space = chr(ord(character))
        return space
    else:
        return character


# create function that convert and entire string in lower or upper case letter
def to_lower(strings):
    result = ""

    for letter in strings:
        if is_upper(letter):
            result += f"{get_lower(letter)}"
        else:
            result += f"{letter}"
        result = result

    return result


def to_upper(strings):
    result = ""

    for letter in strings:
        if is_lower(letter):
            result += f"{get_upper(letter)}"
        else:
            result += f"{letter}"
        result = result

    return result


# create a function that convert string of character with alternate uppercase letter
def alternate_uppercase(strings):
    first_letter = get_upper(strings[0])
    second_letter = get_lower(strings[1])
    result = f"{first_letter}{second_letter}"

    for i in range(2, len(strings)):
        if is_upper(result[i - 1]):
            result += f"{to_lower(strings[i])}"
        elif is_lower(result[i - 1]):
            result += f"{to_upper(strings[i])}"
        elif is_space(result[i - 1]):
            if is_upper(result[i - 2]):
                result += f"{to_lower(strings[i])}"
            else:
                result += f"{to_upper(strings[i])}"
        else:
            continue
        result = result

    return result


print(alternate_uppercase(string))


# create a function that only put first letter of an entire string in upper
def to_upper_first_letter(strings):
    string_with_first_upper_letter = ""
    first_letter = get_upper(strings[0])
    string_with_first_upper_letter += f"{first_letter}"

    for i in range(1, len(strings)):
        if is_upper(strings[i]):
            other_letter = to_lower(strings[i])
            string_with_first_upper_letter += f"{other_letter}"
        else:
            string_with_first_upper_letter += f"{strings[i]}"

    return string_with_first_upper_letter


print(to_upper_first_letter(string))