# -*- coding: utf-8 -*-
"""
LeetCode #1 两数之和
给定一个整数数组 nums 和一个整数目标值 target，
请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。

难度：简单
标签：数组、哈希表
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        解法1：暴力枚举
        时间复杂度：O(n²)
        空间复杂度：O(1)
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
    def twoSum_hash(self, nums: List[int], target: int) -> List[int]:
        """
        解法2：哈希表（推荐）
        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        seen = {}  # 值 -> 下标
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        
        return []

# 测试
if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"输入: nums={nums1}, target={target1}")
    print(f"输出: {solution.twoSum(nums1, target1)}")
    print(f"哈希表解法: {solution.twoSum_hash(nums1, target1)}")
    
    # 测试用例2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"\n输入: nums={nums2}, target={target2}")
    print(f"输出: {solution.twoSum(nums2, target2)}")
