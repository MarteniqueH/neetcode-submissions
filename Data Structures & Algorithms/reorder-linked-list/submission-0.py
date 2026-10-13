# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Start both pointers at the beginning of the linked list.
        # A pointer is simply a variable that keeps track of a node.
        slow = head
        fast = head

        # STEP 1: Find the middle of the linked list.
        #
        # The slow pointer moves forward by 1 node each time.
        # The fast pointer moves forward by 2 nodes each time.
        #
        # Because fast moves twice as quickly as slow, when fast
        # reaches the end of the list, slow will be around the middle.
        #
        # We check fast.next as well because fast moves forward
        # by two nodes, so both fast and the next node must exist.
        while fast and fast.next:
            slow = slow.next          # Move slow forward by 1 node.
            fast = fast.next.next     # Move fast forward by 2 nodes.


        # STEP 2: Split the linked list into two halves.
        #
        # slow is at the middle of the list.
        # slow.next is the first node of the second half.
        # We save that node in Second so we can access the second half.
        Second = slow.next

        # Disconnect the two halves by setting slow.next to None.
        # This means the first half now ends at slow.
        # The second half is still accessible through Second.
        slow.next = None


        # STEP 3: Reverse the second half of the linked list.
        #
        # prev keeps track of the previous node.
        # curr keeps track of the current node we are reversing.
        #
        # Initially, prev is None because the last node of the
        # reversed list must point to None.
        # curr starts at the beginning of the second half.
        prev = None
        curr = Second

        # Continue until curr reaches None, meaning we have
        # reversed every node in the second half.
        while curr:

            # Save the next node before changing any links.
            # Otherwise, we could lose access to the rest of the list.
            nxt = curr.next

            # Reverse the link so the current node points backward
            # to the previous node instead of forward to the next node.
            curr.next = prev

            # Move prev forward to the current node.
            # This node is now the first node of the reversed portion.
            prev = curr

            # Move curr forward to the next node we saved earlier.
            # We use nxt because curr.next has already been changed.
            curr = nxt

        # When the loop finishes, prev points to the beginning
        # of the reversed second half.
        Second = prev

        # first points to the beginning of the original first half.
        first = head


        # STEP 4: Merge the two halves by alternating their nodes.
        #
        # We take one node from the first half, then one node
        # from the reversed second half, repeating until Second
        # has no more nodes.
        while Second:

            # Save the next node in the first half.
            # We need this because first.next will be changed below.
            temp1 = first.next

            # Save the next node in the reversed second half.
            # We need this because Second.next will also be changed.
            temp2 = Second.next

            # Connect the current first-half node to the current
            # second-half node.
            first.next = Second

            # Connect the second-half node to the next node
            # from the original first half.
            # This inserts Second between first and temp1.
            Second.next = temp1

            # Move first forward to the next unused node
            # from the original first half.
            first = temp1

            # Move Second forward to the next unused node
            # from the reversed second half.
            Second = temp2