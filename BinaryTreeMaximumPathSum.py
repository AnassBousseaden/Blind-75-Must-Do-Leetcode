from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# maxPathLeft: Optional[int], maxPathRight: Optional[int], maxPathTree: Optional[int]


class Solution:
    def maxPathFromRoot(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return root.val + max(self.maxPathFromRoot(root.left), self.maxPathFromRoot(root.right), 0)

    def maxPathLeft(self, root: Optional[TreeNode]) -> int:
        return self.maxPathFromRoot(root.left)

    def maxPathRight(self, root: Optional[TreeNode]) -> int:
        return self.maxPathFromRoot(root.right)

    def maxPathSum1(self, root: Optional[TreeNode]):
        if not root:
            return -1001, -1001
        LeftMaxPathResult, LeftMaxPath = self.maxPathSum1(root.left)
        RightMaxPathResult, RightMaxPath = self.maxPathSum1(root.right)
        MaxPathResult = max(root.val + max(LeftMaxPath, 0) +
                            max(RightMaxPath, 0), LeftMaxPathResult, RightMaxPathResult)
        MaxPath = max(root.val, root.val + max(LeftMaxPath, 0),
                      root.val + max(RightMaxPath, 0))
        return MaxPathResult, MaxPath

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.maxPathSum1(root)[0]


test = Solution()

tree = TreeNode(9, TreeNode(6), TreeNode(-3, TreeNode(-6),
                TreeNode(2, TreeNode(2, TreeNode(-6, TreeNode(-6)), TreeNode(-6)))))

tree2 = TreeNode(-3)

print(test.maxPathSum(tree2))
