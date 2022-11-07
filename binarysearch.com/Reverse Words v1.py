class Solution:
    def solve(self, sentence):
        s = ''
        arr = list(sentence.split())
        for i in arr:
            s = i + ' ' + s
        return s.strip()