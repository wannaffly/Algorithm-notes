# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 14:29:12 2021

@author: fly
"""

# =============================================================================
# 136. 只出现一次的数字
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。
# 找出那个只出现了一次的元素。
# [4,1,2,1,2]
# =============================================================================


class Solution:
    def singleNumber(self, nums):
        '''
        将数据保存在字典中 key:元素,value:元素出现次数
        找出出现一次的元素
        '''
        d = dict()
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else: 
                d[nums[i]] = d[nums[i]] +1
        for k,v in d.items():
            if v == 1:
                return k
            
            
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for num in nums:
            a = a ^ num 
            #异或 2 ^ 3 ^ 2 ^ 4 ^ 4等价于 2 ^ 2 ^ 4 ^ 4 ^ 3 => 0 ^ 0 ^3 => 3
        return a
    
    
#return sum(set(nums)) * 2 - sum(nums)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)

        i = 0
        while i < len(nums):
            if i == len(nums)-1:
                return nums[i]
            elif nums[i] == nums[i+1]:
                i += 2
            else:
                return nums[i]









