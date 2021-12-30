from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "[" + str(self.val) + " left : " + self.left.__str__() + " ;  right :" + self.right.__str__() + "]"

# complexity is in O(n²) but we can do O(n) using a hashmap (index,values)


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if preorder == [] or inorder == []:
            return None
        rootValue = preorder[0]
        k = 0
        while True:
            if inorder[k] == rootValue:
                break
            k += 1
        inorderLeft = inorder[0:k]
        inorderRight = inorder[k+1:]
        preorderLeft = preorder[1:k+1]
        preorderRight = preorder[k+1:]
        print(inorderLeft, inorderRight, preorderLeft, preorderRight)
        leftTree = self.buildTree(preorderLeft, inorderLeft)
        rightTree = self.buildTree(preorderRight, inorderRight)
        return TreeNode(rootValue, leftTree, rightTree)


test = Solution()

perorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

print(test.buildTree(perorder, inorder))
