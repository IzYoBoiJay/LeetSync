class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # Volume length * height

        # Length is right index - left index
        # Height is the minimum between the two

        # Idea is to move one of the pointers inward if their height is smaller than the other

        # Keep track of the maximum amount
        max_amount = 0

        left = 0
        right = len(height) - 1

        # While traversing inwardd
        while left < right:

            # Calculate the volume argument values by calculating the length with the minimum height
            length = right - left
            min_height = min(height[left], height[right])

            # Calculate the volume
            volume = length * min_height

            # Take the max amount
            max_amount = max(volume, max_amount)

            # Move left pointer right if shorter
            if height[left] < height[right]:

                left += 1

            # Otherwise move the right pointer left
            else:

                right -= 1

        # Return the max amount
        # O(n) Time Complexity using Two-Pointers and O(1) space complexity as constant number of variables
        return max_amount