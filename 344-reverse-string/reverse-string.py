class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # Base case, a length of 1 is already reversed
        if len(s) == 1:
            return
        
        # Two Pointers, Constant Variables, O(1) Space
        left = 0
        right = len(s) - 1

        # While left pointer is positionally less than right pointer
        while left < right:

            # Swap
            s[left], s[right] = s[right], s[left]

            # Move the two pointers
            left += 1
            right -= 1

        # Time Complexity O(n)