from test_framework import generic_test
import math

def square_root(x):
    # TODO - you fill in here.
    right = x
    left = 0
    if x < 1.0:
        left, right = x, 1.0
    while not math.isclose(left, right):
        med = (right+left)/2
        med_squared = med * med
        if med_squared > x:
            right = med
        else:
            left = med
    return left


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("real_square_root.py",
                                       'real_square_root.tsv', square_root))
