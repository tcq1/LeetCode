from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Solve cycle detection problem with slow and fast pointer. Both pointers start at head, with fast pointer
        progressing twice as fast as slow pointer. If fast pointer catches up with slow pointer there is a cycle, if
        fast pointer reaches end of list there is no cycle.

        :param head: head of list
        :return: ListNode beginning the cycle
        """
        slow = head
        fast = head

        # iterate through list
        while fast is not None and fast.next is not None:
            # progress pointers
            slow = slow.next
            fast = fast.next.next

            # check for equality
            if slow == fast:
                # cycle exists -> find start
                slow2 = head
                while slow != slow2:
                    slow = slow.next
                    slow2 = slow2.next

                return slow

        return None
