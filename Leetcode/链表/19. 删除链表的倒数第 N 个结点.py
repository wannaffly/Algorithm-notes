# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# =============================================================================
# 19. 删除链表的倒数第 N 个结点
# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
# =============================================================================


#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# =============================================================================
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
# =============================================================================
        
head1 = ListNode(1)
head = head1
for i in [2,3,4,5]:
    head1.next = ListNode(i)
    head1 = head1.next
n = 2

# =============================================================================
#快慢指针法(一次遍历)
# =============================================================================

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        q = head
        for i in range(n):
            #需要考虑删除的是头节点的情况
            if p:
                return head.next
            else:
                p = p.next
        
        while p.next:
            p = p.next
            q = q.next
        q.next = q.next.next
        
        
        return head

s = Solution()
a = s.removeNthFromEnd(head,n)

# =============================================================================
#两次遍历
# =============================================================================

      
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        i = 0
        p = head
        #遍历获取链表节点个数
        while p:
            i = i+1
            p = p.next
        
        p = head
        j = 1
        while j < i-n:
            j = j+1
            p = p.next
        if p == head and i == n:
            return head.next
        else:
            p.next = p.next.next
            return head

head = ListNode(1)
head1 = ListNode(2)
head.next = head1
n = 1
        
s = Solution()
a = s.removeNthFromEnd(head,n)

while a:
    print(a.val)
    a = a.next    

    