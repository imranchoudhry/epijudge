from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x):
    # TODO - you fill in here.
    #stack = []
    flag = False
    if x <0:
        flag = True
        x = abs(x)
    t = '0123456789'
    if x == 0:
        return t[x]
    result = ''
    while x:
        rem = x % 10
        x = x//10
        result = t[rem] + result # dont do this
        #stack.insert(0, rem)
    if flag:
        result = '-' + result
    return result


def string_to_int(s):
    # TODO - you fill in here.
    flag = False
    if s[0]=='-':
        flag = True
        s = s[1:]

    power = len(s)
    t = '0123456789'
    result = 0
    for digit in s:
        power -=  1
        digit = t.index(digit)
        result += digit * 10**(power)
    if flag:
        result = result * -1
    return result


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
