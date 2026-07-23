# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        g_nodes = 0

        def findGoodNodes(root, max_node):
            nonlocal g_nodes
            if root:
                if max_node <= root.val:
                    g_nodes += 1
                max_node = max(max_node, root.val)
                findGoodNodes(root.left, max_node)
                findGoodNodes(root.right, max_node)
        findGoodNodes(root, root.val)
        return g_nodes