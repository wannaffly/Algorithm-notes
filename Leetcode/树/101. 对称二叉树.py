# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 10:03:02 2021

@author: fly
"""

# =============================================================================
# 101. 对称二叉树
# 给定一个二叉树，检查它是否是镜像对称的。
# 
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
# =============================================================================


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#递归yyds
class Solution:
    def isSymmetric1(self, root: TreeNode) -> bool:
        if not root :
            return True
        def isSame(left, right):
            # 递归结束条件：
            # 1. 两个节点都为空
            # 2. 一个为空，另一个非空
            # 3. 都为非空，但是值不相等
            # 4. 都为非空，但是值相等（再次进入递归）
            if not (left or right):
                return True
            elif not (left and right):
                return False
            elif left.val != right.val:
                return False
            else: return isSame(left.left,right.right) and isSame(left.right,right.left)
        
        return isSame(root.left,root.right)
    
#队列
    def isSymmetric2(self, root: TreeNode) -> bool:
        q = []
        q.append(root)
        q.append(root)
        while len(q) != 0:
            t1 = q.pop()
            t2 = q.pop()
            if not t1 and not t2:
                continue
            elif t1 == None or t2 == None:
                return False
            else:
                if t1.val != t2.val:
                    return False
                else:
                    q.append(t1.left)
                    q.append(t2.right)
                    q.append(t1.right)
                    q.append(t2.left)
        return True
    
#层次遍历判断是否回文
    def isSymmetric3(self, root: TreeNode) -> bool:
        if not root:
            return True
        parentList = [root]
        while parentList:
            childList = []
            val = []
            for node in parentList:
                if node:
                    val.append(node.val)
                    childList.append(node.left)
                    childList.append(node.right)
                else:
                    val.append('#')
            if val!=val[::-1]:
                return False
            parentList = childList
        return True
    
        

