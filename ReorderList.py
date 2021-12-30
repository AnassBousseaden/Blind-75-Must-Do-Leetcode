from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __str__(self) -> str:
        return str(self.val) + " " + str(self.next)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currNode, leftList = head, None
        while currNode is not None:
            tmp = currNode.next
            currNode.next = leftList
            leftList = currNode
            currNode = tmp
        return leftList

    def reorderList(self, head: Optional[ListNode]) -> None:
        tmp = head
        midNode = head
        prev = None
        while tmp is not None and tmp.next is not None:
            tmp = (tmp.next).next
            prev = midNode
            midNode = midNode.next
        prev .next = None
        l1 = head
        l2 = self.reverseList(midNode)
        while l1 is not None:
            print("l1 : ", l1, "l2 : ", l2)
            nextL1 = l1.next
            nextL2 = l2.next
            l1.next = l2
            if nextL1 is not None:
                l2.next = nextL1
            l1 = nextL1
            l2 = nextL2
        print(head)


test = Solution()


l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print(test.reorderList(l))
