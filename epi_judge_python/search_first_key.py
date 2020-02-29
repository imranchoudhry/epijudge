from test_framework import generic_test


def search_first_of_k(A, k):
    # TODO - you fill in here.
    high, low = len(A) - 1, 0
    while high >= low:
        med = (high + low)//2
        med_elt = A[med]
        if med_elt == k:
            #print(med)
            while med > 0 and A[med -1] == A[med]:
                #print(med)
                med -= 1
            return med
        if k < med_elt:
            high = med - 1
        elif med_elt < k:
            low = med + 1
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
