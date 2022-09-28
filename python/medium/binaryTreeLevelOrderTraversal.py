# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """ Use extension of BFS algorithm using a FIFO queue.

        :param root: Root of tree
        :return: traversal order per level
        """
        if root is None:
            return []

        output = []
        queue = [[root]]

        while queue:
            current_level = []
            next_level = []
            for element in queue.pop(0):
                # add value to current level
                current_level.append(element.val)
                # add nodes to next level
                if element.left:
                    next_level.append(element.left)
                if element.right:
                    next_level.append(element.right)
            # add to output and queue
            output.append(current_level)
            if next_level:
                queue.append(next_level)

        return output


# create nodes
node1 = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)

# set children
node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5

solution = Solution()
print(solution.levelOrder(node1))
