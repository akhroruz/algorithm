class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_ll(head):
    tmp = head
    while tmp:
        print(tmp.val, end=' ')
        tmp = tmp.next


def list_to_ll(a):
    head = ListNode(0)
    tmp = head

    for i in a:
        tmp.next = ListNode(i)
        tmp = tmp.next

    return head.next


# head = [1,2,3,3,4,4,5]
#
# head = list_to_ll(head)
# k = head.val
# tmp = head.next
# print(k)
# while tmp:
#     if tmp.val == k:
#         tmp = tmp.next
#     # tmp = tmp.next
# print_ll(head)

'''
1 2 3 
1 3 2
3 1 2
3 2 1
2 3 1
2 1 3

'''

names = ["Mary", "John", "Emma"]
heights = [180, 165, 170]

# k, n = 0, 0
# for i in range(len(heights)):
#     if k < heights[i]:
#         heights[i] = k
#         k = heights[i]
# print(heights)

print()
