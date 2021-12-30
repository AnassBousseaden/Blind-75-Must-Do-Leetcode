from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currNode, leftList = head, None
        while currNode is not None:
            tmp = currNode.next
            currNode.next = leftList
            leftList = currNode
            currNode = tmp
        return leftList

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head is not None:
            if head.val == None:
                return True
            print(head.val)
            head.val = None
            head = head.next
        return False


test = Solution()
