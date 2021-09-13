# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 16:12:27 2021

@author: fly
"""
# =============================================================================
# 2.两数相加
# 
# 给你两个非空的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，
# 并且每个节点只能存储一位数字。
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
# =============================================================================


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


# =============================================================================
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
# =============================================================================

l = ListNode(9)
l1 = l 
for elem in [9,9,9,9]:
    l.next = ListNode(elem)
    l = l.next   

l = ListNode(9)
l2 = l
for elem in [9,9,9,9,9,9]:
    l.next = ListNode(elem)
    l = l.next

       
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        re = ListNode(0)
        re_start = re
        add = 0
        while l1 and l2:
            full = l1.val + l2.val + add   
            re.next = ListNode(full%10)
            re = re.next
            add = full // 10 #取整
            l1 = l1.next
            l2 = l2.next
            
            
        while l1 is None and l2:
            full = l2.val + add
            re.next = ListNode(full%10)
            re = re.next
            add = full // 10
            l2 = l2.next
        
        while l2 is None and l1:
            full = l1.val + add
            re.next = ListNode(full%10)
            add = full // 10
            re = re.next
            l1 = l1.next
        
        if add:
            re.next = ListNode(add)

        return re_start.next
            
s = Solution()
a = s.addTwoNumbers(l1, l2)        

#一个while解决   
class Solution:
    def addTwoNumbers(self, l1, l2):
        re = ListNode(0)
        re_start = re
        add = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            full =  x + y + add
            re.next = ListNode(full%10)
            re = re.next
            add = full // 10 #取整
            if l1 : l1 = l1.next
            if l2 : l2 = l2.next
        
        if add:
            re.next = ListNode(add)
        
        return re_start.next
             
    
    
    