"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        leftmost = root
        while leftmost:
            cur = leftmost
            leftmost = None
            pre = None

            while cur:
                if cur.left:
                    if not leftmost:
                        leftmost = cur.left
                    if pre:
                        pre.next = cur.left
                    pre = cur.left
                if cur.right:
                    if not leftmost:
                        leftmost = cur.right
                    if pre:
                        pre.next = cur.right
                    pre = cur.right
                cur = cur.next
        return root
        """if not root:
            return None
        queue = deque([root])
        while queue:
            pre = None
            for _ in range(len(queue)):
                cur = queue.popleft()
                if pre:
                    pre.next = cur
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                pre = cur
        return root"""