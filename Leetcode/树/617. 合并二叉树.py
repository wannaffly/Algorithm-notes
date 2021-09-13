# 给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

# 你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，
# 否则不为 NULL 的节点将直接作为新二叉树的节点。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:        
        if root1 and root2:
            root1.val = root1.val + root2.val
            root1.left = self.mergeTrees(root1.left,root2.left)
            root1.right = self.mergeTrees(root1.right,root2.right)
        return root1 or root2