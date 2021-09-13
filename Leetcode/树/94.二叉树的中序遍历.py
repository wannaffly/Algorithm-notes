# 中序遍历 先遍历左子树->根节点->右子树

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

class Solution:
	def preorderTraversal(self, root):
		ret, stack = [], [root]
		while stack:
			node = stack.pop()#pop最后一个元素
			if node:
				ret.append(node.val)
				#注意压入栈的顺序,先压入右孩子，再压入左孩子
				stack.append(node.right)
				stack.append(node.left)
		return ret

    # def inorderTraversal(self, root):
    

    #     # 非递归过程即:先访问..最左子树..结点，再访问其父节点，再访问其兄弟
    #     # while循环条件 中序遍历需先判断当前结点是否存在，若存在则将该节点放入栈中，再将当前结点设置为结点的左孩子，
    #     # 若不存在则取栈顶元素为cur，当且仅当栈空cur也为空，循环结束。
    #     stack, ret = [], []
    #     cur = root
    #     while stack or cur:
    #         if cur:
    #             stack.append(cur)
    #             cur = cur.left
    #         else:
    #             cur = stack.pop()
    #             ret.append(cur.val)
    #             cur = cur.right
    #     return ret
    
    # def postorderTraversal(self, root):
    #     ret, stack = [], []
    #     while root or stack:
    #         if root:
    #             stack.append(root)
    #             ret.insert(0, root.val)
    #             root = root.right
    #         else:
    #             node = stack.pop()
    #             root = node.left
    #     return ret

    # def postorderTraversal(self, root):
    #     res, stack = [], [root]
    #     while stack:
    #         node=stack.pop()
    #         if node:
    #             res.append(node.val)
    #             stack.append(node.left)
    #             stack.append(node.right)
    #     return res[::-1]

# 如果是递归做法则递归遍历左子树，访问根节点，递归遍历右子树

    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     mid = []
    #     if not root:
    #         return []
    #     def inorder(root):
    #         if root.left:
    #             inorder(root.left)
    #         mid.append(root.val)
    #         if root.right:
    #             inorder(root.right)
    #     inorder(root)
    #     return mid