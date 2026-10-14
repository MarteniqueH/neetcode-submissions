"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Create a dictionary that will map each original node to its copied node.
        # None: None allows us to safely handle None references (such as the end of a list).
        oldToCopy = {None: None}

        # Start at the head (the first node) of the original linked list.
        curr = head

        # Loop through the original linked list until curr becomes None.
        while curr:

            # Create a new node with the same value as the current original node.
            # This creates a copy of the node, but does not connect it to other nodes yet.
            copy = Node(curr.val)

            # Store the relationship between the original node and its copy.
            # The original node is the key, and the copied node is the value.
            oldToCopy[curr] = copy

            # Move to the next node in the original linked list.
            curr = curr.next


        # Start again at the head of the original linked list.
        # We need a second pass to connect the copied nodes.
        curr = head

        # Loop through the original linked list again.
        while curr:

            # Find the copy of the current original node using the dictionary.
            copy = oldToCopy[curr]

            # Connect the copied node to the copy of the original node's next node.
            # If curr.next is None, oldToCopy[curr.next] returns None.
            copy.next = oldToCopy[curr.next]

            # Connect the copied node to the copy of the original node's random node.
            # If curr.random is None, oldToCopy[curr.random] returns None.
            copy.random = oldToCopy[curr.random]

            # Move to the next node in the original linked list.
            curr = curr.next


        # Return the copied version of the head node.
        # This gives us the beginning of the completely copied linked list.
        return oldToCopy[head]