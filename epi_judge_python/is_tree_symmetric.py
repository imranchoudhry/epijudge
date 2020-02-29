from test_framework import generic_test


def is_symmetric(tree):
    # TODO - you fill in here.
    if tree:
        return helper(tree.left, tree.right)
        #return tree.left.data == tree.right.data
        #and is_symmetric(tree.left) and is_symmetric(tree.right)
    return True

def helper(node1, node2):
    if not node1 and not node2:
        return True
    if node1 and node2:
        return node1.data == node2.data \
        and helper(node1.right, node2.left) \
        and helper(node1.left, node2.right)
    else:
        return False

def inorder(node, l):
    if node:
        inorder(node.left, l)
        #print(node)
        l.append(node.data)
        inorder(node.right, l)

def is_symmetric2(tree):
    # TODO - you fill in here.
    left_subtree = []
    right_subtree = []


    if tree:
        inorder(tree.left, left_subtree)
        inorder(tree.right, right_subtree)
        print("right_subtree:", right_subtree)
        print("left_subtree", left_subtree)
        return right_subtree==left_subtree[::-1]


    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
