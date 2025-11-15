# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Idea: The approach is similar to two pointers traversing through both linked lists. Compare the
        # value at each node traversal and continue to the next for the appended. The lists themselves are
        # already sorted from lowest to greatest which allows us to do comparison

        # Time complexity is O(n + m) where n is the size of List 1 and m is the size of List 2
        # and that we have the traverse through both entirely in the worst case scenario

        # Space complexity is O(1) because we are simply managing pointers even in the worst case
        
        # Base Case 1: List 1 and List 2 are both empty
        if (list1 is None) and (list2 is None):
            return None
        
        # Base Case 2: List 1 is not empty, but List 2 is empty
        if (list1 is not None) and (list2 is None):
            return list1

        # Base Case 3: List 1 is empty, but List 2 is not empty
        if (list1 is None) and (list2 is not None):
            return list2

        # Create a dummy node for simplification, thus dummy.next is the head
        dummy = ListNode()

        # Keep track of the current node (tail)
        current = dummy

        # While both lists are valid
        while list1 and list2:

            # If the value of list1's node is smaller than list2's node:
            if list1.val < list2.val:

                # The next node is list 1's current node
                current.next = list1

                # Advance list1
                list1 = list1.next

            # Otherwise the value of list2's node is smaller or equivalant to list1's node:
            else:

                # The next node is list 2's current node
                current.next = list2

                # Advance list2
                list2 = list2.next
            
            # Advance the current node to the next node
            current = current.next

        # With the loop broken, check for which list is remaining, and simply "append"

        # If list1 still exists
        if list1:

            # Append the remainder of list1
            current.next = list1

        # If list2 still exists
        elif list2:

            # Append the remainder of list2
            current.next = list2

        # Since the current is pointing to the end or the remainder, but we want the head, we can do so with dummy.next
        return dummy.next