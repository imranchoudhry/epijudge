from test_framework import generic_test


def square_root(k):
    # TODO - you fill in here.
    if k==1: return 1

    def test(input, k):
        return input**2 <=k and (input+1)**2 >k
    
    high = canidate = k//2
    low = 0

    high = k
    i=0
    while low <= high:
        canidate = (high + low)//2
        if test(canidate, k):
            return canidate
        elif canidate**2 < k:
            low = canidate +1
        else:
            high = canidate -1    

    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
