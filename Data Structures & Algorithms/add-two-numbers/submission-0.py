# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
                # Create a dummy node to serve as the starting point of our result linked list.
        # ListNode() creates a node with no value specified (usually 0 or None, depending on the definition).
        dummyNode = ListNode()

        # Set curr to the dummy node so we can build the result list one node at a time.
        curr = dummyNode

        # Start with a carry of 0 because we have not added any digits yet.
        carryValue = 0

        # Keep looping while l1 has nodes, l2 has nodes, or there is still a carry to add.
        while l1 or l2 or carryValue:

            # Get the current digit from l1.
            # If l1 is None (there are no more nodes), use 0 instead.
            v1 = l1.val if l1 else 0

            # Get the current digit from l2.
            # If l2 is None (there are no more nodes), use 0 instead.
            v2 = l2.val if l2 else 0

            # Add both digits and the carry from the previous calculation.
            value = v1 + v2 + carryValue

            # Calculate the carry for the next column using integer division.
            # For example, 15 // 10 = 1, so we carry 1 to the next column.
            carryValue = value // 10

            # Keep only the ones digit using the remainder operator.
            # For example, 15 % 10 = 5, so we store 5 in the current node.
            value = value % 10

            # Create a new node containing the digit we just calculated.
            # Attach it to the end of our result linked list.
            curr.next = ListNode(value)

            # Move curr forward to the new node so we can attach the next digit.
            curr = curr.next

            # Move l1 to its next node if one exists.
            # Otherwise, keep l1 as None.
            l1 = l1.next if l1 else None

            # Move l2 to its next node if one exists.
            # Otherwise, keep l2 as None.
            l2 = l2.next if l2 else None

        # Return the actual result list, skipping the dummy node at the beginning.
        return dummyNode.next



            

        

        
        