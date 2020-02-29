from test_framework import generic_test


def apply_permutation(perm, A):
    # TODO - you fill in here.
    n = len(A)
    #while perm!=list(sorted(perm)):
    for i in range(n):
        while perm[i] != i:
        #print(i)
            target_position = perm[i]
            #print("BEFORE")
            #print("A is ", A)
            #print("perm is ", perm)
            A[i], A[target_position] = A[target_position], A[i]
            perm[i], perm[target_position] = perm[target_position], perm[i]
            #print("AFTER")
            #print("A is ", A)
            #print("perm is ", perm)
    return


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("apply_permutation.py",
                                       "apply_permutation.tsv",
                                       apply_permutation_wrapper))
