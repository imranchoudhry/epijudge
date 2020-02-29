from test_framework import generic_test
from binary_tree_node import BinaryTreeNode

preorder_pointer = 0

def get_subtree(preorder, indorder, node, side):

    idx = indorder.index(node)
    if side==left:
        return indorder[:idx]
    else:
        return indorder[idx+1:]


def helper(preorder, inorder, start, end):
    if start > end:
        return None
        
    global preorder_pointer
    print(preorder_pointer)
    root = preorder[preorder_pointer]
    preorder_pointer += 1

    if start==end:
        return BinaryTreeNode(data = root)

    root_idx = inorder.index(root)

    left_node = helper(preorder, inorder, start, root_idx-1)
    right_node = helper(preorder, inorder, root_idx+1, end)
    root_node = BinaryTreeNode(data = root, left = left_node, right = right_node)

    return root_node


def helper2(preorder_iter, inorder):
    inorder_idx = {data: i for i, data in enumerate(inorder)}

    if inorder:
        root = next(preorder_iter)
        root_idx = inorder_idx[root]
        left_node = helper2(preorder_iter, inorder[:root_idx])
        right_node = helper2(preorder_iter, inorder[root_idx+1:])

        root_node = BinaryTreeNode(data = root, left = left_node, right = right_node)
        return root_node

def binary_tree_from_preorder_inorder(preorder, inorder):
    preorder_iter = iter(preorder)
    return helper2(preorder_iter, inorder)


def binary_tree_from_preorder_inorder3(preorder, inorder):
    inorder_idx = {data: i for i, data in enumerate(inorder)}
    if inorder:
        root = preorder.pop(0)
        inorder_idx
        root_idx = inorder_idx[root]
        left_node = binary_tree_from_preorder_inorder(preorder, inorder[:root_idx])
        right_node = binary_tree_from_preorder_inorder(preorder, inorder[root_idx+1:])
        root_node = BinaryTreeNode(data = root, left = left_node, right = right_node)
        return root_node


def binary_tree_from_preorder_inorder2(preorder, inorder):

    start = 0
    end = len(preorder)-1
    preorder_pointer = 0
    return helper(preorder, inorder, start, end)
    # TODO - you fill in here.
    return None


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))