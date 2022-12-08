# https://leetcode.com/problems/richest-customer-wealth/
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        a = []
        for i in accounts:
            a.append(sum(i))
        return max(a)
