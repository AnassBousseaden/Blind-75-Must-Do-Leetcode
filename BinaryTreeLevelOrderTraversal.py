from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        queue = []
        if root != None:
            queue.append(root)
        result = []
        while queue != []:
            tmp = []
            l = []
            while queue != []:
                subtree = queue.pop(0)
                left = subtree.left
                right = subtree.right
                l.append(subtree.val)
                if left != None:
                    tmp.append(left)
                if right != None:
                    tmp.append(right)
            result.append(l)
            queue = tmp
        return result


test = Solution()

tree = TreeNode(5, TreeNode(3), TreeNode(7))


print(test.levelOrder(None))
