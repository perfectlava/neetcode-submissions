# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1V = 0
        ind1 = 1
        
        l2V = 0
        ind2 = 1

        while l1 or l2:
            if l1 != None:
                l1V += l1.val * ind1
                ind1 *= 10
                l1 = l1.next

            if l2 != None:
                l2V += l2.val * ind2
                ind2 *= 10
                l2 = l2.next
        
        result = l1V + l2V
        dummy = curr = ListNode(-999)
        curr.next = ListNode(0)

        while result != 0:
            curr.next = ListNode(val = result % 10) # 975 % 10 = 5
            result = result // 10  # 975 // 10 = 97 // 10 = 9 // 10 = 0
            curr = curr.next

        return dummy.next 



