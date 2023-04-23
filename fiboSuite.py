from sys import argv
from sys import exit


# conditioning argument
arg = argv[1]


# function(s)
def fibo_reference_index(x):
    # print Fibonacci number from list, with user entry as reference
    x += 1
    fibo = [0] * x
    fibo[0] = 0
    fibo[1] = 1
    for i in range(2, x):
        fibo[i] = fibo[i-1] + fibo[i-2]
    x -= 1
    print(fibo[x])


# errors in user entry
try:
    arg = int(arg)
except ValueError:
    print("Error -1")
    exit(1)
if arg < 0:
    print("Error -1")
    exit(1)
if len(argv) > 2:
    print("Error -1")
    exit(1)


fibo_reference_index(arg)