# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        a = []
        for i in sentences:
            a.append(len(list(i.split())))
        return max(a)
