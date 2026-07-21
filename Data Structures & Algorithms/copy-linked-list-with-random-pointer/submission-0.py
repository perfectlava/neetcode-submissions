"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        Map = {}
        newMap = {}
        curr = head
        i = 0
        
        curr = head
        dummy = currD = Node(-999)

        while curr:
            currD.next = Node(x=curr.val, random=curr.random)
            Map[curr] = i
            
            currD = currD.next
            curr = curr.next
            newMap[i] = currD
            i += 1
        

        currD = dummy.next

        while currD:
            
            if currD.random:
                rIndex = Map[currD.random]
                rNode  = newMap[rIndex]
                currD.random = rNode
            
            currD = currD.next
        
        return dummy.next




