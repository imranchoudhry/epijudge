from test_framework import generic_test


def roman_to_integer(s):
    # TODO - you fill in here.

    t={"I":1, "V":5, "X":10, "L":50, "C":100, "D": 500, "M":1000}

    int_sum = 0
    prev = "M"
    for roman_numeral in s:
        if t[roman_numeral] > t[prev]:
            int_sum -= (2* (t[prev]))
        int_sum += t[roman_numeral]
        prev = roman_numeral


    return int_sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "roman_to_integer.py", 'roman_to_integer.tsv', roman_to_integer))
