class Solution:
    def solve(self, sentence):
        arr = sentence.split()
        arr.reverse()
        return ' '.join(arr)