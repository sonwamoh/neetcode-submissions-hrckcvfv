# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            leftDepth = dfs(root.left)
            rightDepth = dfs(root.right)

            if abs(leftDepth - rightDepth) > 1:
                self.balanced = False
            
            return 1 + max(leftDepth, rightDepth)
        
        dfs(root)
        return self.balanced

        