# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 10:19:59 2021

@author: fly
"""
# =============================================================================
# 206. 反转链表
# 反转一个单链表。
# 示例:
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# =============================================================================

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode(1)
l = head
for i in [2,3,4,5]:
    l1 = ListNode(i)
    l.next = l1
    l = l1

# =============================================================================
# 遍历
# =============================================================================
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head         
        re = head
        h = re.next
        re.next = None
        while h:
            p = h.next
            h.next = re
            re,h = h,p
        return re
    
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p, rev = head, None
        while p:
            rev, rev.next, p = p, rev, p.next
        return rev



class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        造新节点
        """
        cur = None      
        while head:
            cur = ListNode(head.val, cur)
            head = head.next
        return cur















