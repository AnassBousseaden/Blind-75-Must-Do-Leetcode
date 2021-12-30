from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isValidBST(self, root: Optional[TreeNode], inf: Optional[int] = None, sup: Optional[int] = None) -> bool:
        if root == None:
            return True
        if not inf == None and root.val <= inf:
            return False
        if not sup == None and root.val >= sup:
            return False
        # le node est valide
        left = self.isValidBST(root.left, inf, root.val)
        right = self.isValidBST(root.right, root.val, sup)
        return left and right


test = Solution()

tree = TreeNode(5, TreeNode(3), TreeNode(7))

print(test.isValidBST(tree))
