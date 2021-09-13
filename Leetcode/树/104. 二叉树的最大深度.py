# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 14:46:25 2021

@author: fly
"""

# =============================================================================
# 104. 二叉树的最大深度
# 给定一个二叉树，找出其最大深度。
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 说明: 叶子节点是指没有子节点的节点。
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]返回它的最大深度 3 。
# =============================================================================


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
l1 = TreeNode(9)
l2 = TreeNode(20)
s1 = TreeNode(15)
s2 = TreeNode(7)

root.left = l1
root.right = l2
l2.left = s1
l2.right = s2


class Solution:
    # 递归解法1
    def maxDepth1(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return max(self.maxDepth1(root.left), self.maxDepth1(root.right)) + 1
    # 递归解法2

    def maxDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.maxDepth2(root.left)
        right = self.maxDepth2(root.right)
        return max(left, right) + 1

    # 广度优先遍历BFS(Breadth First Search)
    def maxDepth3(self, root: TreeNode) -> int:
        if not root:
            return 0
        parentList = [root]
        i = -1
        while parentList:
            childList = []
            for node in parentList:
                if node:
                    childList.append(node.left)
                    childList.append(node.right)
            i = i + 1
            parentList = childList
        return i
        
    def maxDepth4(self, root: TreeNode) -> int:
        if root == None:
            return 0
        stack, depth = [], 0
        stack.append((1, root))
        while stack:
            cur, node = stack.pop()
            if node:
                depth = max(depth, cur)
                stack.append((cur+1, node.left))
                stack.append((cur+1, node.right))
        return depth


s = Solution()
print(s.maxDepth4(root))
