# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        first = root.val
        self.ans = float('inf')

        def dfs(node):
            if not node:
                return
            if first < node.val < self.ans:
                self.ans = node.val
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.ans if self.ans < float('inf') else -1
