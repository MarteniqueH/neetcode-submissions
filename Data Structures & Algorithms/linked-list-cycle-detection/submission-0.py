# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
                # Use two pointers to check if the linked list has a cycle.

        # The slow pointer starts at the head of the linked list.
        # It moves forward one node at a time.
        slow = head

        # The fast pointer also starts at the head.
        # It moves forward two nodes at a time.
        fast = head

        # Keep looping as long as:
        # 1. fast is not None (we haven't reached the end).
        # 2. fast.next is not None (fast can safely move two steps).
        while fast and fast.next:

            # Move slow forward by ONE node.
            slow = slow.next

            # Move fast forward by TWO nodes.
            fast = fast.next.next

            # Check if both pointers are pointing to the SAME node.
            # If they meet, the linked list contains a cycle.
            if slow == fast:
                return True

        # If fast reaches the end of the list, there is no cycle.
        return False