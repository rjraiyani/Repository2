import sys

def last_digit(a, b):
#    "Find the last digit of a^b"
#    pass #TODO: Replace pass with your code
    p = 0

    p = a**b

    o = p % 10

    print(o)
    return


a, b = map(int, sys.stdin.readline().split())

print(last_digit(a, b))
