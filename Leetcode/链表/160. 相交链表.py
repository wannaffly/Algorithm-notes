# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 09:38:07 2021

@author: fly
"""

# =============================================================================
# 160. 相交链表
# 编写一个程序，找到两个单链表相交的起始节点。
# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
# 输出：Reference of the node with value = 8
# 输入解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
# 从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
# 在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
# =============================================================================

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        '''
        计算两个链表的长度，长的链表先走差值，遍历链表直到相交
        '''
        i = 0
        p = headA
        while p:
            i = i + 1
            p = p.next
            
        j = 0
        q = headB
        while q:
            j = j + 1
            q = q.next
        
        if i > j:
            for m in range(i-j):
                headA = headA.next
        if j > i:
            for m in range(j-i):
                headB = headB.next
        
        while headA:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None
    
    
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        使两个链表到达相等位置时走过的是相同的距离
        链表1的长度是x1+y，链表2的长度是x2+y，我们同时遍历链表1和链表2，到达末尾时，再指向另一个链表。
        则当两链表走到相等的位置时：x1+y+x2 = x2+y+x1
        """
        p = headA
        q = headB
        while p!=q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p 



        
        
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        把headA的元素放入字典中
        遍历headB看元素在不在字典中
        """
        d = dict()
        while headA:
            d[headA] = 1
            headA = headA.next
        while headB:
            if headB in d:
                return headB
            else:
                headB = headB.next
        return None
    