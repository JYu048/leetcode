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
        
        # Find Middle
        fast, slow = head.next, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next    
        
        right = slow.next
        slow.next = None

        # Reverse slow list
        prev, curr = None, right

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # merge left and right list
        left, right = head, prev

        while right:
            next_left = left.next
            next_right = right.next

            left.next = right
            left.next = right
            right.next = next_left

            left, right = next_left, next_right
        
        return left


# Time: O(N)
# Space: O(1)



# Optimal Solution (from chatgpt)

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
        
        # find middle
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        # reverse right half
        prev, curr = None, slow

        while curr:
            next_node = curr.next
            curr.next = prev
            prev, curr = curr, next_node
        
        # Merge two lists
        left, right = head, prev

        while right.next:
            next_left, next_right = left.next, right.next

            left.next = right
            right.next = next_left

            left, right = next_left, next_right
        
        return head

        
        
        

        