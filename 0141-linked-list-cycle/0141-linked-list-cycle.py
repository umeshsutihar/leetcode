# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        # Traverse the list. Fast moves 2 steps, slow moves 1 step.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If they meet, there is a cycle.
            if slow == fast:
                return True
                
        # If fast reaches the end of the list (None), there's no cycle.
        return False
        