# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        q = deque([root])
        ltr = True
        while q:
            size = len(q)
            temp = [0] * size
            for i in range(size):
                node = q.popleft()
                index = i if ltr else (size - 1 -i)
                temp[index] = node.val
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
            ltr = not ltr
            result.append(temp)
        return result