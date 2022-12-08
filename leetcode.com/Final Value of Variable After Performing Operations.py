# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        n = 0
        for i in range(len(operations)):
            if operations[i] in ["X++", "++X"]:
                n += 1
            else:
                n -= 1
        return n