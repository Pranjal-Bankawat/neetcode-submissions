# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs_balanced(root):
            if not root:
                return 0
            left = dfs_balanced(root.left)
            if left == -1:
                return -1
            right = dfs_balanced(root.right)
            if right == -1:
                return -1
            balanced = abs(left - right)
            if balanced > 1:
                return -1

            return 1 + max(left,right)
        return dfs_balanced(root) != -1