from test_framework import generic_test

def get_height(node):
    if not node:
        return (-1, True)
    lh = get_height(node.left)
    rh = get_height(node.right)
    if lh[1] is False or rh[1] is False:
        return (0, False)

    is_balanced = (abs(lh[0] - rh[0]) <= 1)
    ch = 1 + max(lh[0], rh[0])
    return (ch, is_balanced)
    #return 1 + max(get_height(node.left), get_height(node.right))  

def is_balanced_binary_tree(tree):
    # TODO - you fill in here.
    if tree:
        lh = get_height(tree.left)
        if lh[1] is False:
            return False
        
        rh = get_height(tree.right)
        if rh[1] is False:
            return False

        is_balanced = (abs(lh[0] - rh[0]) <= 1)
        return is_balanced

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
