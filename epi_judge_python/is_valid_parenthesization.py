from test_framework import generic_test


def is_well_formed(s):
    # TODO - you fill in here.

    parens = {'}':'{', ')':'(', ']':'['}

    stack = []

    for char in s:
        if char not in parens:
            stack.append(char)
        elif char in parens:
            if not stack:
                return False
            top_of_stack = stack.pop()
            if parens[char]!=top_of_stack:
                return False
    if not stack:
        return True
    else:
        return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_parenthesization.py",
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
