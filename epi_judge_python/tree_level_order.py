from test_framework import generic_test


def binary_tree_depth_order(tree):
    # TODO - you fill in here.
    if not tree:
        return []
    q1 = []
    result = []
    q1.append(tree)
    while True:
        curr_level= []
        next_level = []
        next_level_empty = True
        while q1:
            
            popped_node = q1.pop(0)

            if popped_node.left:
                next_level.append(popped_node.left)
                next_level_empty = False
            if popped_node.right:
                next_level.append(popped_node.right)
                next_level_empty = False
            curr_level.append(popped_node.data)
        result.append(curr_level)
        q1.extend(next_level)
        if next_level_empty:
            break
    

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
