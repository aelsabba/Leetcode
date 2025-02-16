# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1
# 2 3

# 1 -> 2 = 12
# 1 -> 3 = 15

#                1 
#               2 3
#             4 5 6 7
# 7= 7
# 3 -> [1 2 5] = 8
# 1
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        local_total = 0

        def dfs(node):
            nonlocal total
            nonlocal local_total

            local_total = (local_total * 10) + node.val

            if not node.left and not node.right:
                total += local_total
                print(local_total)

            if node.left:
                dfs(node.left)  # dfs(2)

            if node.right:
                dfs(node.right)

            local_total = (local_total - node.val) / 10  # 1

            return None

        dfs(root)  # dfs(1)

        return int(total)