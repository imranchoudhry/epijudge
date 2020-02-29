from test_framework import generic_test


def inorder_traversal(tree):
    result = []
    prev = None
    while tree:
        if prev == tree.parent:
            if tree.left:
                prev = tree
                tree = tree.left
            else:
                result.append(tree.data)
                if tree.right:
                    prev = tree
                    tree = tree.right
                else:
                    prev = tree
                    tree = tree.parent
        elif prev == tree.right:
            prev = tree
            tree = tree.parent
        else:
            result.append(tree.data)
            prev = tree
            if tree.right:
                tree = tree.right
            else:
                tree = tree.parent

    # TODO - you fill in here.
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_with_parent_inorder.py",
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
