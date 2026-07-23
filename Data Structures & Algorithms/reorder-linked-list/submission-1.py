# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        s2 = slow.next
        prevPtr = slow.next = None

        while s2:
            tmp = s2.next
            s2.next = prevPtr
            prevPtr = s2
            s2 = tmp
        
        s1, s2 = head, prevPtr

        while s2:
            tmp1, tmp2 = s1.next, s2.next
            s1.next = s2
            s2.next = tmp1
            s1, s2 = tmp1, tmp2





