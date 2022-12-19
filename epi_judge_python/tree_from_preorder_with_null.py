import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:
    # TODO - you fill in here.
    ## ----- THE FOLLOWING CODE WILL NEVER WORK -------- BECAUSE THE APPROACH IS FLAWED
    node_array = [None for x in preorder]
    for index, node_value in enumerate(preorder):
        if node_value:
            node_array[index] = BinaryTreeNode(node_value)
    def helper(i):
        if not node_array[i]:
            return 
        if 2*i+1 < len(node_array):
            node_array[i].left = node_array[2*i+1]
            helper(2*i+1)
        if 2*i+2 < len(node_array):
            node_array[i].right = node_array[2*i+2]
            helper(2*i+2)
    helper(0)
    # print(node_array[0].left)
    return node_array[0]


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_with_null.py',
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))
