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
from collections import Counter
# l = [2,3,4,5]
# root = Node(1)
# for i in l:
#     add(root, i)

from string import ascii_lowercase, ascii_uppercase, digits
# s = "A man, a plan, a canal: Panama"
# s1 = [i for i in s if i in ascii_lowercase or i in ascii_uppercase or i in digits]
# print(''.join(i for i in s1[::-1]).lower() == ''.join(i for i in s1).lower())

# a = [-4, -1, 0, 3, 10]
# l = len(a) - 1
#
# while l > 0:
#     if abs(a[0]) > abs(a[l]):
#         a[0], a[l] = a[l], a[0]
#     else:
#         pass

nums = [4,5,6,7,0,1,2]
k = 3
d = {}
try:
    print(nums.index(k))
except ValueError as e:
    print(-1)
