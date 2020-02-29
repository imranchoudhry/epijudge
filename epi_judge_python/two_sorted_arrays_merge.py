from test_framework import generic_test


def merge_two_sorted_arrays(A, m, B, n):
    # TODO - you fill in here.

    overall_index = m + n -1
    a_index = m - 1
    b_index = n - 1

    while (a_index >= 0) and (b_index >= 0):
        if A[a_index] >= B[b_index]:
            A[overall_index] = A[a_index]
            overall_index -= 1
            a_index -=1
        else:
            A[overall_index] = B[b_index]
            overall_index -= 1
            b_index -= 1
    """
    while a_index >= 0:
        A[overall_index] = A[a_index]
        overall_index -= 1
        a_index -=1
    """
    while b_index >= 0:
        A[overall_index] = B[b_index]
        overall_index -= 1
        b_index -= 1

    return


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sorted_arrays_merge.py",
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
