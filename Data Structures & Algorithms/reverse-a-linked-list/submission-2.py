# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prevPtr = None
        nextPtr = None

        while curr != None:
            nextPtr = curr.next
            curr.next = prevPtr
            prevPtr = curr
            curr = nextPtr
        
        return prevPtr