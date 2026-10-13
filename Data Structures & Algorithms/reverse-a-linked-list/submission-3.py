# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
                # Reverse a linked list iteratively by flipping one pointer at a time.
        # We want each node to point to the node BEFORE it instead of AFTER it.

        # Keep track of the previous node.
        # Initially, there is no previous node, so prev is None.
        prev = None

        # Start at the first node of the linked list.
        curr = head

        # Continue until curr reaches the end of the list (None).
        while curr:

            # Save the next node before changing any pointers.
            # We need this because we are about to change curr.next.
            nxt = curr.next

            # Reverse the pointer!
            # Instead of pointing to the next node, curr now points backward
            # to the previous node.
            curr.next = prev

            # Move prev forward to the current node.
            # This node is now the previous node for the next iteration.
            prev = curr

            # Move curr forward using nxt, which we saved earlier.
            # This lets us continue through the original list.
            curr = nxt

        # When curr becomes None, we have reached the end of the original list.
        # prev now points to the new first node of the reversed list.
        return prev
        


        