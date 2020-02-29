from test_framework import generic_test


def even_odd_merge(L):
    # TODO - you fill in here.
    if not L:
        return None
    even = even_head = L
    if L.next:
        odd_head = odd = L.next
    else:
        return L

    while odd.next and odd.next.next:
        even.next = odd.next
        odd.next = odd.next.next

        even = even.next
        odd = odd.next

    #ended in even
    if odd.next:
        even.next = odd.next
        odd.next = None
        even = even.next
        even.next = odd_head
        return L
    
    #ended in odd
    even.next = odd_head
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_list_merge.py",
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
