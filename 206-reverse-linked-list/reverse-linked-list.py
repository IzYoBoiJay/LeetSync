# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # The idea is to keep track of the previous node and next node, flip the current
        # node's next pointer to the previous, and then continue repeating with the next node
        # until next is None

        # Base case 1: There are no nodes
        if head is None:
            return None

        # Base case 2: If there is only a single node
        if head.next is None:
            return head

        # Perform the reversal node operation which is O(n), where n is size of linked list
        # Let the current be the head node and previous node be None
        current_node = head
        previous_node = None

        # Iterate through each node while the curr node is still valid
        while current_node:

            # Let temp_node be the current's next node
            temp_node = current_node.next

            # Set the current node's next pointer to the previous node
            current_node.next = previous_node

            # Let the previous node be the current_node
            previous_node = current_node

            # Let the current node now be the next node stored in the temp_node
            current_node = temp_node

        # Return the previous_node which is now the head of the linked list
        # O(n) time complexity
        # O(1) space complexity
        return previous_node