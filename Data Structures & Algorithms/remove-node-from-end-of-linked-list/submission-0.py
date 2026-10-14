# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
                # Create a fake node (0) before the list.
        # This makes it easier to remove the first node if needed.
        dummy = ListNode(0, head)

        # left starts at the fake node.
        left = dummy

        # right starts at the first real node.
        right = head


        # Move right forward n times.
        # This creates a gap of n nodes between left and right.
        while n > 0:
            right = right.next  # Move right to the next node.
            n -= 1              # We moved once, so subtract 1 from n.


        # Move both pointers forward together.
        # Stop when right reaches the end of the list.
        while right:
            left = left.next    # Move left forward one node.
            right = right.next  # Move right forward one node.


        # Remove the node immediately after left.
        # Make left point to the node AFTER the one being removed.
        left.next = left.next.next


        # Return the updated list.
        # Skip the fake node and return the real first node.
        return dummy.next
        