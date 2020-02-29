from test_framework import generic_test


def add_two_numbers(L1, L2):

    dummy_head = ListNode()
    return None

def add_two_numbers2(L1, L2):
    # TODO - you fill in here.
    results = []
    max_len = 0
    for i in reversed(range(len(L2))):
        result = [0] * i
        [0] * i
        for j in reversed(range(len(L1))):
            result = [L2[i] * L1[j]] + result
        max_len = max(len(result), max_len)
        results.append(result)
    #for i in reversed(range(max_len)):
        
    return None


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_list_add.py",
                                       'int_as_list_add.tsv', add_two_numbers))
