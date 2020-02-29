from test_framework import generic_test


def search_smallest(A):
    # TODO - you fill in here.
    if A[-1] > A[0]: return 0
    high, low = len(A)-1, 0
    minimum = float('inf')
    while high >= low:
        mid = (high + low)//2
        if A[mid] >= A[low]: # the left side of the array is normally sorted
            min_index = low if A[low] < minimum else min_index
            minimum = min(A[low],minimum)
            low = mid + 1
        elif A[mid] < A[low]:
            min_index = mid if A[mid] < minimum else min_index
            minimum = min(A[mid], minimum)
            high = mid - 1
    return min_index


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_shifted_sorted_array.py",
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
