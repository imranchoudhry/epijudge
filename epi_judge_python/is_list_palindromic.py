from test_framework import generic_test

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def is_linked_list_a_palindrome(L):
    # TODO - you fill in here.
    head = L
    dummy = dummy_head = ListNode(0)

    while L:
        dummy.next = L
        dummy = dummy.next
        L = L.next
    
    #reverse the duplicated list

    #dummy_head.next = D
    prev = None
    curr = dummy_head.next
    print(dummy_head.next)
    print(curr.next)
    while curr:
        next_up = curr.next
        curr.next = prev
        prev = curr
        curr = next_up
    
    D = dummy_head.next

    while D and L:
        #print(D.data + " " + L.data)
        if D.data != L.data:
            return False
        D = D.next
        L = L.next
    
    return True


    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_list_palindromic.py",
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
