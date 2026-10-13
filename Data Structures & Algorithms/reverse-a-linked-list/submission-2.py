# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#reversing the linked list iteratively by flipping pointers one step at a time 

#Move through the list left to right 
#The next pointer will redirect pointers to point to the node behind it. 

        #The node that comes after the current node once reversed
        prev = None 

        #The current node processing
        curr = head 

        while curr: 
            #the original next node
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev


#moving pointers forward each step the list is gradually revese the entire list 

# the curr becoems number the list. is ffull reverses
