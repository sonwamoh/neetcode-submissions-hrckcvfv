
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
            1. edge case handling
                if not root: return []
                if only root, return root
            2. Use queue to simulate lvl order traversal
            3. you curr len of queue, to track nodes in specific lvl
            4. push node at respective lvl inside a inner arr
            TC: O(n), to iterate all nodes
            SC: O(n)
        """
        if not root:
            return []
        
        q = deque([root])

        res = []

        while q:
            n = len(q)
            curr_lvl = []

            for _ in range(n):
                curr = q.popleft()
                curr_lvl.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(curr_lvl)

        return res           


    

        