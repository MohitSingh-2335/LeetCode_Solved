# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if (head == None):
            return False
        tur , rab = head , head
        while (rab != None and rab.next != None):
            rab = rab.next.next
            tur = tur.next
            if (tur == rab):
                return True
        return False