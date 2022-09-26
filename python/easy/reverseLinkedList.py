# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        # call recursive function
        return self.recursiveReverseList(head, None)

    def recursiveReverseList(self, current: Optional[ListNode], prev: Optional[ListNode]) -> Optional[ListNode]:
        # if end of linked list reached make it head
        if current.next is None:
            return ListNode(val=current.val, next=prev)

        # recursive call
        next_node = current.next
        current.next = prev

        return self.recursiveReverseList(next_node, current)


a, b, c, d = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
a.next = b
b.next = c
c.next = d

solution = Solution()
reversed_head = solution.reverseList(None)
print(reversed_head)
