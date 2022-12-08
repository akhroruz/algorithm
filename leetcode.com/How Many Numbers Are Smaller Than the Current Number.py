# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        return [sorted(nums).index(i) for i in nums]