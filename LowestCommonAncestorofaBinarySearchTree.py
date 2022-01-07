from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p1 = min(p.val, q.val)
        p2 = max(p.val, q.val)
        if root.val == p1 or root.val == p2:
            return root

        m = root.val
        if p1 < m and m < p2:
            return root
        if m < p1:
            return self.lowestCommonAncestor(root.right, p, q)
        return self.lowestCommonAncestor(root.left, p, q)


test = Solution()

tree = TreeNode(5, TreeNode(3), TreeNode(7))
