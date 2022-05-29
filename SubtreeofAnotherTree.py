# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # naive solution :
    def equal(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None or subRoot == None:
            return root == subRoot
        if root.val != subRoot.val:
            return False
        equalLeft = self.equal(root.left, subRoot.left)
        equalRight = self.equal(root.right, subRoot.right)
        return equalLeft and equalRight

    def isSubtreeNaive(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot == None:
            return True
        if root == None:
            return False
        equal = self.equal(root, subRoot)
        if equal:
            return True
        return self.isSubtree(root.left, subRoot.left) or self.isSubtree(root.right, subRoot.right)
    # possibilité de faire l'égalité en utilisant un arble de merkel est une fonction de hachage bien choisit
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


test = Solution()
tree = TreeNode(3, TreeNode(4, TreeNode(
    1), TreeNode(2, None, TreeNode(0))), TreeNode(5))
