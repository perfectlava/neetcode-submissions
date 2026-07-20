# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        revHead = None
        curr = head
        length = 0
        
        while curr:
            revHead = ListNode(curr.val, revHead)    
            curr = curr.next
            length += 1

        revCurr = revHead
        curr = head
        dummy = ListNode("Dummy")
        dumbCurr = dummy
        i = 0

        while i < length:
            if i % 2:
                dumbCurr.next = revCurr
                revCurr = revCurr.next
            else:
                dumbCurr.next = curr
                curr = curr.next
        
            dumbCurr = dumbCurr.next
            dumbCurr.next = None
            i += 1
        
        head = dummy.next



            