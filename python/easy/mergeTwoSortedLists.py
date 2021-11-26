from typing import Optional


class ListNode:
    """ Class representing linked lists.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(list_node):
    """ Print list nodes

    :param list_node: head of list
    """
    if list_node:
        current_node = list_node

        while current_node.next:
            print('Node: {} - Next: {}'.format(current_node.val, current_node.next.val))
            current_node = current_node.next


class Solution:
    """ Class containing solution to task of merging two linked lists.
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            next_node = list1 if list1.val <= list2.val else list2
            head = ListNode(next_node.val, None)
            if next_node is list1:
                head.next = self.mergeTwoLists(next_node.next, list2)
            else:
                head.next = self.mergeTwoLists(list1, next_node.next)

            return head


nodes = [ListNode(i) for i in range(10)]
for i in range(len(nodes)):
    try:
        nodes[i].next = nodes[i+2]
    except IndexError:
        pass

solution = Solution()
print(print_list(solution.mergeTwoLists(nodes[1], nodes[2])))
