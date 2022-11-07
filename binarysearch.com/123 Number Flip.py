class Solution:
      def solve(self, n):
         l = list(str(n))
         for m in range(len(l)):
            if l[m] != '3':
               l[m] = '3'
               return int(''.join(l))
         return n