# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 08:17:15 2021

@author: fly
"""
# =============================================================================
# 141. 环形链表
# 给定一个链表，判断链表中是否有环。
# 
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 
# 如果 pos 是 -1，则在该链表中没有环。
# 注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
# 如果链表中存在环，则返回 true 。 否则，返回 false 。
# =============================================================================




# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



# =============================================================================
# 最容易想到的方法是遍历所有节点，每次遍历到一个节点时，判断该节点此前是否被访问过。
# 具体地，我们可以使用哈希表来存储所有已经访问过的节点。
# 每次我们到达一个节点，如果该节点已经存在于哈希表中，则说明该链表是环形链表，否则就将该节点加入哈希表中。
# 重复这一过程，直到我们遍历完整个链表即可。
# =============================================================================

#记录在字典中
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        re = head
        map = dict()
        while re:
            if re.next in map:
                return True
            else:
                map[re.next] = re.val
            re = re.next
        return False
    
#记录在集合中
class Solution:
    def hasCycle(self, head: ListNode) -> bool:            
        hash_set = set()
        while head:
            if head in hash_set:
                return True
            hash_set.add(head)
            head = head.next
        return False


# =============================================================================
# 快慢指针
# 为什么fast 走两个节点，slow走一个节点，有环的话，一定会在环内相遇呢，而不是永远的错开呢？
# fast指针一定先进入环中，如果fast 指针和slow指针相遇的话，一定是在环中相遇，这是毋庸置疑的。
# 这是因为fast是走两步，slow是走一步，其实相对于slow来说，fast是一个节点一个节点的靠近slow的，
# 所以fast一定可以和slow重合。
# =============================================================================

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
            
            
            
            
            
            
            
            
            
            
            