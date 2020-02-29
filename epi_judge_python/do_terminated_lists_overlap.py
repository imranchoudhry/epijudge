import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0, l1):
    # TODO - you fill in here.
    l0_head = l0
    l1_head = l1
    l0_len = 0
    if not l1 or not l0:
        return None
    while l0.next:
        l0 = l0.next
        l0_len += 1
    l1_len = 0
    while l1.next:
        l1 = l1.next
        l1_len += 1
    if l1 is not l0:
        return None
    if l0_len >= l1_len:
        for _ in range(l0_len-l1_len):
            l0_head = l0_head.next
    elif l1_len > l0_len:
        for _ in range(l1_len - l0_len):
            l1_head = l1_head.next
    while l1_head is not l0_head:
        l1_head, l0_head = l1_head.next, l0_head.next
    return l0_head
        


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(
        functools.partial(overlapping_no_cycle_lists, l0, l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_terminated_lists_overlap.py",
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
