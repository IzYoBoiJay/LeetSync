class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        # O(n) Time Complexity & O(n) Space Complexity
        
        # Create a new array of size 2n, where n is size of nums
        new_arr = [0 for x in range(len(nums) * 2)]

        # Iterate through nums
        for i in range(len(nums)):

            # Set new_arr[i] and new_arr[i + n] to nums[i]
            new_arr[i] = nums[i]
            new_arr[i + len(nums)] = nums[i]

        # Return result
        return new_arr