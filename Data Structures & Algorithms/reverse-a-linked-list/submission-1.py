# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        prev, curr, temp
        0 -> 1 -> 2 -> 3
    P   H    N
        """
        curr = head
        prev = None

        while curr:
            temp = curr.next # next node
            curr.next = prev # change the pointer of curr to prev
            prev = curr # make prev = curr
            curr = temp # iterate curr to next
        return prev
        