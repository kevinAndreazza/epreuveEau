

def get_arguments(array):
    return array[1:]

def mini_maxi_len_of(array, mini, maxi=None):

    if maxi is None:
        if len(array) < mini:
            return False
        else:
            return True
    else:
        if len(array) > maxi or len(array) < mini:
            return False
        else:
            return True

def display_error_in(function):
    if not function:
        print("error")
        exit(1)
    else:
        pass

def verify_len(array, mini_len, maxi_len=None):
    display_error_in(mini_maxi_len_of(array, mini_len, maxi_len))


