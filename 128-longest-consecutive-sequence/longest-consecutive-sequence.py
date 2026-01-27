class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Base case from constraint, if length is 0
        if len(nums) == 0:
            return 0
        # Second base case from constraint, if length is 1
        elif len(nums) == 1:
            return 1

        # Convert nums to a set O(n)
        set_nums = set(nums)

        # Keep track of longest consecutive sequence
        longest_sequence_length = 0

        # For each number in the set
        for num in set_nums:

            # If the current number does not have a preceding value, such that it is the start of a sequence
            if (num - 1) not in set_nums:

                # Get the current number and begin the sequence count
                current_num = num
                sequence_count = 1

                # While there exists the next number in the set of nums
                while (current_num + 1) in set_nums:

                    # Iterate the current number
                    current_num += 1

                    # Add to the sequence count
                    sequence_count += 1

                # Once the loop is broken such that there is no consecutive number, compare the current longest sequence length and the sequence count
                # and take the maximum of the two
                longest_sequence_length = max(longest_sequence_length, sequence_count)

        # Return thte longest sequence length
        return longest_sequence_length


            