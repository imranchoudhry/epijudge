from test_framework import generic_test


def plus_one(A):
    # TODO - you fill in here.
    last_digit = A[-1] + 1
    if last_digit <10:
        return A[:-1] + [last_digit]
    curr_digit = last_digit
    curr = -1
    while curr_digit==10 and ((curr*-1)<len(A)):
        last_digit = 0
        A[curr] = last_digit
        curr_digit = A[curr -1]
        curr_digit += 1
        curr -= 1
    if curr_digit==10:
        A = [1,0] + A[1:]
    else:
        A[curr] = curr_digit
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
