from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):

    # TODO - you fill in here.

    def get_next_elt_index(curr_index, array):
        curr_elt = array[curr_index]
        curr_index += 1
        while curr_index < len(array):
            if array[curr_index] != curr_elt:
                return curr_index
            curr_index += 1
        return None

    intersect = []

    if not A or not B:
        return intersect
    
    i = j = 0

    while i is not None and j is not None:
        if A[i] == B[j]:
            intersect.append(A[i])
            i = get_next_elt_index(i, A)
            j = get_next_elt_index(j,B)
        elif A[i] < B[j]:
            i = get_next_elt_index(i, A)
        else:
            j = get_next_elt_index(j, B)

    return intersect


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
