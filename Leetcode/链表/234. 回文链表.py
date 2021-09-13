# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 10:45:47 2021

@author: fly
"""
# =============================================================================
# 234. 回文链表
# 请判断一个链表是否为回文链表。
# 输入: 1->2->2->1
# 输出: true
# =============================================================================


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
head = ListNode(1)
l = head
for i in [1,2,1]:
    l1 = ListNode(i)
    l.next = l1
    l = l1
        
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 快慢指针找到链表中点
        p = head
        q = head
        
        while p.next and p.next.next:
            p = p.next.next
            q = q.next
            
        #将慢指针之后链表反转
        h = q.next
        q.next = None
        while h:            
            l = h.next
            h.next = q
            q,h = h,l
            
        #比较是否为回文数
        while head != q and q.next != head:
            if head.val == q.val:                
                head = head.next
                q = q.next
            else:
                return False
        #中位数有两个时比较这两个数
        if head.val != q.val:
            return False
        return True
    
s = Solution()
a = s.isPalindrome(head)
        
            
        