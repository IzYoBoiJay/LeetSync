class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) == 1:

            return

        left = 0
        right = 1

        while right < len(nums):

            while nums[left] != 0 and left < right:

                left += 1

            if nums[right] != 0:

                nums[left], nums[right] = nums[right], nums[left]

                left += 1
            
            right += 1

