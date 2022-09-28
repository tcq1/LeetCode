# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        """ Get preorder with simple DFS using a LIFO stack.

        :param root: root of tree
        :return: list of nodes in preorder traversal order
        """
        if root is None:
            return []

        output = []
        # stack
        stack = [root]

        # while stack not empty traverse through tree
        while len(stack) > 0:
            # get current top of stack
            current_node = stack.pop()
            output.append(current_node.val)

            # add children to stack
            if current_node.children is not None:
                current_node.children.reverse()
                for child in current_node.children:
                    stack.append(child)

        return output


# create nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

# set children
node3.children = [node5, node6]
node1.children = [node3, node2, node4]

solution = Solution()
print(solution.preorder(node1))
