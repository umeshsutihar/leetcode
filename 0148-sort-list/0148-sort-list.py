# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return head
        
        pairs = []
        p = head
        while p:
            pairs.append((p.val, p))
            p = p.next
        
        sorted_pairs = sorted(pairs, key=lambda x: x[0])
        # rebuild 
        for i in range(len(pairs) - 1):
            sorted_pairs[i][1].next = sorted_pairs[i+1][1]
        sorted_pairs[-1][1].next = None
        return sorted_pairs[0][1]