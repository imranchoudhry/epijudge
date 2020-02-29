from test_framework import generic_test

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def merge_two_sorted_lists(L1, L2):
    # TODO - you fill in here.
    head = ListNode()
    dum_head = head
    while L1 and L2:
        if L1.data < L2.data:
            head.next = L1
            head = head.next
            L1 = L1.next if L1.next else None
        else:
            head.next = L2
            head = head.next
            L2 = L2.next if L2.next else None
    
    if  L2:
        head.next = L2
    else:
        head.next = L1

    return dum_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
