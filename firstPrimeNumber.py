from sys import argv
from sys import exit


arg = argv[1]


# functions
def est_premier(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def next_sup_prime_number(x):
    y = x + 1
    while not est_premier(y):
        y += 1
    else:
        print(y)

# errors in user entry
try:
    arg = int(arg)
except ValueError:
    print("Error -1")
    exit(1)
if arg < 0:
    print("Error -1")
    exit(1)

next_sup_prime_number(arg)