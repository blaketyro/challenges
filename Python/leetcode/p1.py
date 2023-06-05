# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        looking_for = {}
        for i, num in enumerate(nums):
            if num in looking_for:
                return looking_for[num], i
            looking_for[target - num] = i


def test(*args):
    print(Solution().twoSum(*args))


test([2, 7, 11, 15], 9)
