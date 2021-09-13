# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 21:09:54 2021

@author: fly
"""

# =============================================================================
# 21. 合并两个有序链表
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4] 
# =============================================================================


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
l = ListNode(1)
l1 = l 
for elem in [2,4]:
    l.next = ListNode(elem)
    l = l.next   

l = ListNode(1)
l2 = l
for elem in [3,4]:
    l.next = ListNode(elem)
    l = l.next
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        head_start = head
        while l1 and l2:  
            if l1.val <= l2.val:
                head.next = l1
                head = head.next
                l1 = l1.next                
            else:
                head.next = l2
                head = head.next
                l2 = l2.next
                
        if l1:
            head.next = l1
        if l2:
            head.next = l2
            
        return head_start.next
    
s = Solution()
a = s.mergeTwoLists(l1,l2)
    
while a:
    print(a.val)
    a = a.next

 #递归方法
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        if pHead1.val < pHead2.val:
            pHead1.next = self.Merge(pHead1.next,pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge(pHead1,pHead2.next)
            return pHead2           