import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


def find_min_max(A):
    # TODO - you fill in here.

    if not A:
        return None
    if len(A)<2:
        return MinMax(min(A), max(A))

    max_overall = min_overall = A[0]

    if len(A)%2==0:
        n = len(A)//2
    else:
        n=len(A)//2 + 1

    for i in range(n):
        #print(i)
        curr = A[2*i:(2*i)+2]
        #print(curr)
        if len(curr) <2:
            max_curr = curr[0]
            min_curr = curr[0]
        elif curr[0] > curr[1]:
            max_curr = curr[0]
            min_curr = curr[1]
        else:
            max_curr = curr[1]
            min_curr = curr[0]
        max_overall = max(max_curr, max_overall)
        min_overall = min(min_curr, min_overall)
        
    return MinMax(min_overall, max_overall)


def res_printer(prop, value):
    def fmt(x):
        return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_for_min_max_in_array.py",
            'search_for_min_max_in_array.tsv',
            find_min_max,
            res_printer=res_printer))
