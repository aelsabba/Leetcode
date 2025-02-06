# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque, defaultdict


class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        if not root or not target:
            return None
        if k == 0:
            return [target.val]

        graph = defaultdict(list)
        queue = deque([root])

        while len(queue) > 0:
            node = queue.popleft()

            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                queue.append(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                queue.append(node.right)

        queue = deque([(target, 0)])
        visited = set([target])
        results = []

        while len(queue) > 0:
            node, level = queue.popleft()

            if level == k:
                results.append(node.val)
            else:
                for edge in graph[node]:
                    if not edge in visited:
                        visited.add(edge)
                        queue.append((edge, level + 1))

        return results