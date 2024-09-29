# Original
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        ptr = dummy
        carry = 0
        res = 0

        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # Add carry value
            if carry: v1 += 1

            # Compute sum and carry
            if (v1 + v2) > 9:
                res = v1 + v2 - 10
                carry = 1
            else:
                res = v1 + v2
                carry = 0
            
            ptr.next = ListNode(res)

            if l1: l1 = l1.next
            if l2: l2 = l2.next
            ptr = ptr.next

            # If carry on last digit, add it to the end
            if not l1 and not l2:
                if carry:
                    ptr.next = ListNode(1)
                break
        

        return dummy.next
            
            
# Optimized
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Dummy node to simplify pointer handling
        ptr = dummy
        carry = 0

        while l1 or l2 or carry:
            # Extract values from the current nodes if available
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Calculate the sum and carry for the current position
            total = v1 + v2 + carry
            carry = total // 10  # Set carry for the next iteration
            ptr.next = ListNode(total % 10)  # Add new node with the sum modulo 10

            # Move pointers
            ptr = ptr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next
        