import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0, node1):
    # find node0's depth
    n = node0
    node0_depth = 0
    while n.parent:
        n = n.parent
        node0_depth += 1

    n = node1
    node1_depth = 0
    while n.parent:
        n = n.parent
        node1_depth += 1

    # which node has the greater depth?
    node0_is_deeper = False
    if node0_depth > node1_depth:
        node0_is_deeper = True

    diff = abs(node0_depth - node1_depth)

    if node0_is_deeper:
        while diff>0:
            node0 = node0.parent
            diff -= 1
    else:
        while diff>0:
            node1 = node1.parent
            diff -= 1

    while node0 != node1:
        node0 = node0.parent
        node1 = node1.parent

    return node0


    # TODO - you fill in here.
    return None


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor_with_parent.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
