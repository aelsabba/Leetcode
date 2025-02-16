# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#          1
#    2           3
# 4     5
#      7   8
# 1 3 5 8
from collections import deque, defaultdict
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        right_view = []
        frontier = deque([root])       # (1,0)
        while len(frontier) > 0:
            next_frontier = []
            right_view.append(frontier[-1].val)
            while len(frontier) > 0:
                node = frontier.popleft()        #(1,0)     # (2,1)
                if node.left:
                    next_frontier.append(node.left) # [(2,1)]
                if node.right:
                    next_frontier.append(node.right) #[(2,1),(3,1)]
            frontier = deque(next_frontier)

        return right_view