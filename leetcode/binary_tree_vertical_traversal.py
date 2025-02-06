# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def bfs(self,node):
        queue = deque([(node,0)])
        nodes = {}
        while len(queue) > 0:
            node, column = queue.popleft()
            if node is not None:
                if column not in nodes:
                    nodes[column] = []
                nodes[column].append(node.val)
                if (node.left):
                    queue.append((node.left,column - 1))
                if (node.right):
                    queue.append((node.right,column + 1))
        return nodes

    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = self.bfs(root)
        return [nodes[key] for key in sorted(nodes.keys())]
