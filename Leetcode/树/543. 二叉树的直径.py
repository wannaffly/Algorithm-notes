# 543. 二叉树的直径
# 给定一棵二叉树，你需要计算它的直径长度。
# 一棵二叉树的直径长度是任意两个结点路径长度中的最大值。
# 这条路径可能穿过也可能不穿过根结点。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def deapth(node):
            nonlocal ma #上一级函数中的局部变量
            if not node:
                return 0
            l = deapth(node.left)
            r = deapth(node.right)
            ma = max(l + r, ma)
            return max(l, r) + 1
        ma = 0
        deapth(root)
        return ma