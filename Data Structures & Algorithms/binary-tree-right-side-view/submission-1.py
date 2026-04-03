# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        res = []

        if not root:
            return []

        while q:
            n = len(q)
            curr = []

            for _ in range(n):
                node = q.popleft()
                curr.append(node)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)

            res.append(curr[-1].val)
        return res
        