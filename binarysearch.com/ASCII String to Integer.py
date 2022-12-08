class Solution:
    def solve(self, s):
        n, summa = '', 0
        for i in s:
            if i.isdigit():
                n += i
            elif n:
                summa += int(n)
                n = ''
        if n:
            summa += int(n)
        return summa
