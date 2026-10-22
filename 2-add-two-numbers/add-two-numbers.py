# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Compute total sum and new carry
            total = val1 + val2 + carry
            carry = total // 10
            
            # Create next node with the single-digit remainder
            current.next = ListNode(total % 10)
            current = current.next
            
            # Advance pointers safely
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy_head.next
