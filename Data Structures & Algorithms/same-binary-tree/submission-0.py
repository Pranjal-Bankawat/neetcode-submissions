# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = True
        def sameTree(p, q):
            nonlocal res
            if (not p and q) or (p and not q):
                res = False
            if not p or not q:
                return
            sameTree(p.left, q.left)
            sameTree(p.right, q.right)

            if p.val != q.val:
                res = False

        sameTree(p,q)
        return res
