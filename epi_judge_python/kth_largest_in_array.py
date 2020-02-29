from test_framework import generic_test
import random

# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k, A):
    # TODO - you fill in here.
    def partition(high, low):
        init_high = high
        pivot_index = random.randint(low, high)
        A[pivot_index], A[high] = A[high], A[pivot_index]
        pivot = A[high]
        equal = low
        for i in range(low, high):
            if A[i] < pivot:
                A[i], A[equal] = A[equal], A[i]
                equal +=1
        A[equal], A[high] = A[high], A[equal]
        """
        while equal < high:
            if A[equal] < pivot:
                A[low], A[equal] = A[equal], A[low]
                low +=1
                equal += 1
            elif A[equal] == pivot:
                equal +=1
            else:
                high -= 1
                A[high], A[equal] = A[equal], A[high]

        A[init_high], A[high] = A[high], A[init_high]
        """

        """
        if (len(A) -high +1)==k:
            A= [pivot]
        elif (len(A) -high) <k:
            A = A[:equal]
        else:
            A = A[equal:]
            print(A)
        """
        return equal



    low = 0
    high = len(A)-1
    returned_index = partition(high, low)
    #print(returned_index)
    while True:
        if len(A) - returned_index == k:
            return A[returned_index]
        elif len(A) - returned_index > k:
            low = returned_index + 1
            returned_index = partition(high, low)
        else:
            high = returned_index-1
            returned_index = partition(high, low)
"""



    while len(A)>1:
        A = partition(A)

    return A[0]
"""


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_largest_in_array.py",
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
