class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


Global1 = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def aux(root, p, q):
            if root == None:
                return False, False
            LeftHasP, LeftHasQ = aux(root.left, p, q)
            RightHasP, RightHasQ = aux(root.right, p, q)
            if (LeftHasP and LeftHasQ):
                return True, True
            if RightHasP and RightHasQ:
                return True, True
            NodeHasP = root.val == p or LeftHasP or RightHasP
            NodeHasQ = root.val == q or LeftHasQ or RightHasQ
            if NodeHasP == True and NodeHasQ == True:
                self.resultValue = root
            return NodeHasP, NodeHasQ
        aux(root, q.val, p.val)
        return self.resultValue


test = Solution()

tree = TreeNode(5, TreeNode(1, TreeNode(2), TreeNode(7)),
                TreeNode(3, TreeNode(9)))


t1 = TreeNode(2, TreeNode(7), TreeNode(4))
t2 = TreeNode(5, TreeNode(6), t1)
t3 = TreeNode(1, TreeNode(0), TreeNode(8))

t = TreeNode(3, t2, t3)

print(test.lowestCommonAncestor(t, t2, t3).val)
