from test_framework import generic_test


def stable_sort_list(L):
    # TODO - you fill in here.
    p, r = 0, len(L)-1

    if p>=r:
        return L
    
    q = (p+r)//2

    stable_sort_list(L[p:q+1])
    stable_sort_list(L[q+1:r+1])

    #merge
    


    return None


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sort_list.py", 'sort_list.tsv',
                                       stable_sort_list))
