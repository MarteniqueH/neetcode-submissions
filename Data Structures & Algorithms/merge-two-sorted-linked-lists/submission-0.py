# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
                # Merge two sorted linked lists into one sorted linked list.
        # list1 and list2 are already sorted in ascending order.

        # Create a dummy node to make it easier to build the merged list.
        # It acts as a starting point, even before we add any real nodes.
        dummyNode = ListNode()

        # The tail keeps track of the last node in our merged list.
        # Initially, it points to the dummy node.
        tail = dummyNode

        # Keep looping while BOTH lists still have nodes to process.
        while list1 and list2:

            # Compare the values at the beginning of both lists.
            # We want to add the smaller value to our merged list first.
            if list1.val < list2.val:

                # Add the current node from list1 to the end of the merged list.
                tail.next = list1

                # Move list1 forward to its next node.
                list1 = list1.next

            else:
                # If list2's value is smaller or equal, add its node instead.
                tail.next = list2

                # Move list2 forward to its next node.
                list2 = list2.next

            # Move tail forward because we just added a node.
            # Tail now points to the last node in the merged list.
            tail = tail.next

        # The loop stops when at least one list is empty.

        # If list1 still has nodes, attach all of them to the merged list.
        # They are already sorted, so we do not need to compare them again.
        if list1:
            tail.next = list1

        # Otherwise, if list2 still has nodes, attach the remaining nodes.
        elif list2:
            tail.next = list2

        # Return the merged list, skipping the dummy node.
        # dummyNode.next points to the first real node in the merged list.
        return dummyNode.next