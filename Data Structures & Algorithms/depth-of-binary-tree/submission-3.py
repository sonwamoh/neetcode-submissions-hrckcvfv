# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 1 + max(depthLeft, depthRight)
        if not root:
            return 0
        
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        return 1 + max(leftDepth, rightDepth)

sol = Solution()
print(sol.maxDepth(TreeNode()))
print(sol.maxDepth(TreeNode(0)))

tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)
tree1.right.left = TreeNode(4)

print(sol.maxDepth(tree1))



        