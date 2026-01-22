class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Idea is to move left pointer when smaller, and move right pointer when larger
        # Taking advantage of predictable dynamics -> inward traversal to find a number
        # [1, 2, 3, 5] 5
        # 1, 5 = 6
        # 1, 3 = 4
        # 2, 3 = 5 indicies

        # Base case: If there is always exactly one solution and constraint is that
        # minimum size 2, then return indices 1 and 2 (as (0+1)..((n-1) + 1) of length 2)
        if len(numbers) == 2:
            return [1, 2]


        # Left pointer at beginning
        left_ptr = 0

        # Right pointer at end
        right_ptr = len(numbers) - 1

        # While the sum of the numbers at the indices do not equal target
        while (numbers[left_ptr] + numbers[right_ptr]) != target:

            # Calculate the sum
            sum_of_indices = numbers[left_ptr] + numbers[right_ptr]

            # If the sum of the indices is less than the target
            if sum_of_indices < target:

                # Move the left pointer forward (increasing)
                left_ptr += 1

            # Otherwise, the sum of the indices is greater than the target
            elif sum_of_indices > target:

                # Move the right pointer back (decreasing)
                right_ptr -= 1

        # At the end of the while loop (condition is met), the target is found
        # so return the indices, that is, the left and right pointers
        # added by one
        return [left_ptr + 1, right_ptr + 1]