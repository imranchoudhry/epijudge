import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.

def delete_duplicates(A):
    if not A:
        return 0
        
    pointer = 0
    for i in range(len(A)-1):
        if A[i]==A[i+1]:
            continue
        else:
            A[pointer] = A[i]
            pointer += 1
    print('w')
    A[pointer] = A[-1]

    pointer+=1
    print(A)
    return pointer



def delete_duplicates2(A):

    if not A:
        return 0

    write_index = 1
    for i in range(1, len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return write_index


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_array_remove_dups.py",
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
