#236 lca
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def lowestCommonAncestorHelper(self, root, p, q, stack, nodesFound):
        if not root:
            return nodesFound
        print("entering node: %d" % root.val)
        appended = False
        if nodesFound == 0:
            stack.append(root)
            appended = True
        if (root == p or root == q):
            nodesFound += 1
        nodesFound = self.lowestCommonAncestorHelper(root.left, p, q, stack, nodesFound)
        if nodesFound == 2:
            return nodesFound
        else:
            nodesFound= self.lowestCommonAncestorHelper(root.right, p, q, stack, nodesFound)
            if nodesFound == 2:
                return nodesFound
        if appended:
            stack.pop()
        return nodesFound

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = []
        nodesFound = self.lowestCommonAncestorHelper(root, p, q, stack, 0)
        if nodesFound < 2:
            return None
        if len(stack) == 0:
            return None
        else:
            return stack[len(stack) - 1]