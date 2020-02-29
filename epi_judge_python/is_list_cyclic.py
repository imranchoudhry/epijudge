import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def has_cycle2(head):
    # TODO - you fill in here.
    curr_node = head
    #s = set()
    l = []
    while curr_node.next:
        if curr_node in l:
        #if curr_node.visited==True:
            return curr_node
        #curr_node.visited= True
        l.append(curr_node)
        curr_node = curr_node.next
    return None

def has_cycle(head):
    # TODO - you fill in here.
    #test if cycle exists
    slow = fast = head
    is_cyclic = False
    count = 0
    while slow.next and (fast.next and fast.next.next):
        slow = slow.next
        fast = fast.next.next
        count += 1
        if slow is fast:
            is_cyclic = True
            break
    if not is_cyclic:
        return None
    
    #its cyclic, so find out the node at the start of the cycle
    first = second = head
    for _ in range(count):
        second = second.next
    while first.data != fast.data:
        first, fast = first.next, fast.next
    
    return first

@enable_executor_hook
def has_cycle_wrapper(executor, head, cycle_idx):
    cycle_length = 0
    if cycle_idx != -1:
        if head is None:
            raise RuntimeError("Can't cycle empty list")
        cycle_start = None
        cursor = head
        while cursor.next is not None:
            if cursor.data == cycle_idx:
                cycle_start = cursor
            cursor = cursor.next
            cycle_length += 1 if cycle_start is not None else 0

        if cursor.data == cycle_idx:
            cycle_start = cursor
        if cycle_start is None:
            raise RuntimeError("Can't find a cycle start")
        cursor.next = cycle_start
        cycle_length += 1

    result = executor.run(functools.partial(has_cycle, head))

    if cycle_idx == -1:
        if result is not None:
            raise TestFailure("Found a non-existing cycle")
    else:
        if result is None:
            raise TestFailure("Existing cycle was not found")
        cursor = result
        while True:
            cursor = cursor.next
            cycle_length -= 1
            if cursor is None or cycle_length < 0:
                raise TestFailure(
                    "Returned node does not belong to the cycle or is not the closest node to the head"
                )
            if cursor is result:
                break

    if cycle_length != 0:
        raise TestFailure(
            "Returned node does not belong to the cycle or is not the closest node to the head"
        )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_list_cyclic.py", 'is_list_cyclic.tsv', has_cycle_wrapper))
