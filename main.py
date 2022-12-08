# from collections import Counter
#
#
# class Node:
#     def __init__(self, value=0, left=None, right=None) -> None:
#         self.value = value
#         self.left = left
#         self.right = right
#
#     def __str__(self) -> str:
#         return f'{self.value}'
#
#
# def add(root, n):
#     if not root:
#         return Node(n)
#     if root.value > n:
#         root.left = add(root.left, n)
#     else:
#         root.right = add(root.right, n)
#     return root
#
#
# def in_order(root):
#     if not root:
#         return
#     in_order(root.left)
#     print(root.value)
#     in_order(root.right)
#
#
# def post_order(root):
#     if not root:
#         return
#     post_order(root.left)
#     post_order(root.right)
#     print(root.value)
#
#
# def pre_order(root):
#     if not root:
#         return
#     print(root.value)
#     pre_order(root.left)
#     pre_order(root.right)
#
#
# def depth(root):
#     if not root:
#         return 0
#     return max(depth(root.left), depth(root.right)) + 1
#
#
# def is_balance(root):
#     if not root:
#         return 0
#     return abs((depth(root.left) + 1) - (depth(root.right) + 1)) < 2
import math
from collections import Counter, defaultdict

# l = [2,3,4,5]
# root = Node(1)
# for i in l:
#     add(root, i)
# s = "abcd"
# t = "abcde"
# s = int(input())
# n = 0
# if s < 10:
#     print(s)
#     exit()
# for i in range(10, s + 1):
#     n += 2
# print(n + 9)

# if s < 10:
#     print(s)
#     exit()
# def findDigits(n):
#     if n == 1:
#         return 1
#     s = str(n)
#     return len(s) + findDigits(n - 1)
#
# # Driver Code
#
# # Given N
# N = 13
#
# # Function call
# print(findDigits(N))

# 3
# 010011
# 0
# 1111000

n = int(input())
a = []
for _ in range(n):
    a.append(input())


for i in a:
    s = i.strip('0')
    print(s.count('0'), sep='\n')



# n = 13
# print(n * (n + 1) // 2)
# s = int(input())
# n = 0
# if s < 10:
#     print(s)
#     exit()
# print(s * len(str(s)) - 9)

# print(pow(10, 9))

# 9
# 90
# 900
# 9000
# 90000
# 900000
# 9000000
# 90000000

# def fun(n):
#     if n == 1:
#         return 1
#     s = str(n)
#     return len(s) + fun(n - 1)
# print(fun(1000))

# def totalDigits(n):
#     if n < 10:
#         return n
#     number_of_digits = 0
#     for i in range(1, n, 10):
#         number_of_digits = (number_of_digits + (n - i + 1))
#     return number_of_digits + 1
