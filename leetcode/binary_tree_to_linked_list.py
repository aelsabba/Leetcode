"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


## solution inspired by cracking FAANG
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        self.last = None
        self.first = None

        self.link_in_order(root)

        self.last.right = self.first
        self.first.left = self.last

        return self.first

    def link_in_order(self, node):
        if node:
            self.link_in_order(node.left)

            if not self.last:
                self.first = node
            else:
                self.last.right = node
                node.left = self.last

            self.last = node

            self.link_in_order(node.right)