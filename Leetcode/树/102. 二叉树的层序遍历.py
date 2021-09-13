# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        parentList = [root]
        layer = []
        while parentList:
            childList = []
            val = []
            for node in parentList:
                if node:
                    val.append(node.val)
                    childList.append(node.left)
                    childList.append(node.right)
            parentList = childList
            if val != []:
                layer.append(val)
        return layer    
