from test_framework import generic_test


def snake_string(s):
    # TODO - you fill in here.
    S2 = ""
    for i in range(1,len(s),4):
        S2 += s[i]
    for i in range(0,len(s),2):
        S2 += s[i]
    for i in range(3,len(s),4):
        S2 += s[i]

    return S2


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("snake_string.py", 'snake_string.tsv',
                                       snake_string))
