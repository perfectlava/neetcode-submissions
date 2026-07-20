# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        
        while curr:
            curr = curr.next
            length += 1
        
        target = length - n 
        print(f"length: {length} target: {target}")
        
        if target <= 0:
            return head.next

        i = 0
        curr = head

        while curr.next:
            i += 1
            if i == target:
                curr.next = curr.next.next
                return head
            curr = curr.next
