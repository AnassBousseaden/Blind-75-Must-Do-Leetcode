from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# NOT MY SOLUTION SEE LEETCODE TO GET THE SOLUTION


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node: Optional[TreeNode]) -> list[int]:
            if node == None:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        return inorder(root)[k-1]


test = Solution()

tree = TreeNode(2, TreeNode(1), TreeNode(3))
tree = TreeNode(5, TreeNode(3, TreeNode(
    2, TreeNode(1)), TreeNode(4)), TreeNode(6))


for i in range(1, 7):
    print(i, end=" :")
    print(test.kthSmallest(tree, i))
