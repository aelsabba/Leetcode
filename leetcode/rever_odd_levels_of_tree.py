# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
############### BFS
from collections import deque


class Solution:
    def swap(self, parent1, parent2):
        temp = parent1.left.val
        parent1.left.val = parent2.right.val
        parent2.right.val = temp
        if parent1 != parent2:
            temp = parent1.right.val
            parent1.right.val = parent2.left.val
            parent2.left.val = temp

    def swap_level(self, parents):
        left = 0
        right = len(parents) - 1
        while left <= right:
            self.swap(parents[left], parents[right])
            left = left + 1
            right = right - 1

    def reverse_bfs(self, root):
        q = deque([(root, 0)])
        current_level_parents = []
        current_level = 0
        while len(q) > 0:
            node, level = q.popleft()
            if (level % 2 == 1 and level != current_level):
                self.swap_level(current_level_parents)
                current_level_parents = []
            elif level != current_level:
                current_level_parents = []
            current_level = level
            current_level_parents.append(node)
            if node.left:
                q.append((node.left, current_level + 1))
            if node.right:
                q.append((node.right, current_level + 1))

    ############ DFS

    def reverse_dfs(self, left, right, level):
        if left == None or right == None:
            return None

        if level % 2 == 0:
            temp = left.val
            left.val = right.val
            right.val = temp

        self.reverse_dfs(left.left, right.right, level + 1)
        self.reverse_dfs(left.right, right.left, level + 1)

    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.reverse_dfs(root.left, root.right, 0)
        return root
