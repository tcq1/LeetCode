from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Use fast and slow pointers to find the middle of a linked list. The fast pointer
        moves twice as fast as the slow pointer, resulting in the slow pointer reaching the middle
        of the list once the fast pointer reaches the end.

        :param head: head of linked list
        :return: middle node
        """
        slow = head
        fast = head

        # go through list with both pointers
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow
