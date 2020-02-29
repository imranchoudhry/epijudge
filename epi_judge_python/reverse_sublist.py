from test_framework import generic_test

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def reverse_sublist(L, start, finish):
    # TODO - you fill in here.
    dummy_head = ListNode()
    dummy_head.next = L
    curr = dummy_head
    for i in range(start-1):
        curr = curr.next

    sublist_head = curr
    curr = sublist_head.next
    for i in range(start, finish):
        next2 = curr.next
        hosl = sublist_head.next
        sublist_head.next = next2
        curr.next = next2.next
        next2.next = hosl

    
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
