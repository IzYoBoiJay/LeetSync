class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Second to last position as last character is neither increasing nor decreasing
        pivot = len(nums) - 2

        # Locate the pivot: While the pivot is >= 0 and that it is larger or equal to than the one to the right of it
        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:

            # Move the pivot left
            pivot -= 1

        # If the pivot is not found, it is in its largest permutation and we need to return the reversed
        if pivot == -1:

            nums.reverse()

        # Otherwise find the rightmost successor to swap with and reverse the remainder
        else:
            
            successor = len(nums) - 1

            # While the successor is less than or equal to the pivot
            while nums[successor] <= nums[pivot]:

                # Move the successfor left
                successor -= 1

            # When the successor is found, swap the pivot and the successor
            nums[pivot], nums[successor] = nums[successor], nums[pivot]

            # Reverse the suffix after the pivot (Python slice here is inclusive pivot + 1 to end)
            nums[pivot + 1:] = reversed(nums[pivot + 1:])