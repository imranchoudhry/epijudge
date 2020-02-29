from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    # TODO - you fill in here.
    head = k_ahead = L 
    for _ in range(k):
        if not k_ahead.next:
            return L.next
        k_ahead = k_ahead.next
    while k_ahead.next:
        L = L.next
        k_ahead = k_ahead.next
    L.next = L.next.next
    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
