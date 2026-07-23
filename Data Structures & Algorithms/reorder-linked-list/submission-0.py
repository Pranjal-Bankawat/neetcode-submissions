# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        #Find the mid of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        s2 = slow.next
        slow.next = None
        s1 = head

        # Reverse the other linked list
        prevPtr = None
        nextPtr = None

        while s2:
            nextPtr = s2.next
            s2.next = prevPtr
            prevPtr = s2
            s2 = nextPtr

        s2 = prevPtr
        # Merge both linked list
        dummy = node = ListNode()

        while s1 and s2:
            temp1, temp2 = s1.next, s2.next
            s1.next = s2
            if temp1:
                s2.next = temp1
            s1 = temp1
            s2 = temp2





