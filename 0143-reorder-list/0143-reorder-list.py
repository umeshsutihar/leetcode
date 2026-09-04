# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
            
        # Step 1: Find the middle of the linked list
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        # Step 2: Reverse the second half of the list
        prev = None
        curr = slow.next
        slow.next = None  # Break the list into two halves
        
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
            
        # Step 3: Merge the two halves alternately
        first = head
        second = prev  # prev is now the head of the reversed second half
        
        while second:
            # Save next pointers
            temp1 = first.next
            temp2 = second.next
            
            # Link first to second, then second to first's next
            first.next = second
            second.next = temp1
            
            # Move forward
            first = temp1
            second = temp2
        