class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Sum must be 0

        # a + b + c = 0
        # If we pivot on one element at a time, we fix on that, choose a
        # Thus b + c = -a

        # Needs predicitive dynamics, sort the array
        # O(nlogn) Time Complexity with O(1) Space Complexity
        nums.sort()

        # Create a set so there are no duplicates
        triplets = []

        # Loop through each element, the element being looped at is a
        for a in range(len(nums)):

            # Base case optimizatoin: Starting element is positive, so there are no solutions that can be 0
            if nums[0] > 0:

                break

            # If the previous element is the same, skip it
            if a > 0 and nums[a] == nums[a - 1]:

                continue

            # Target is -nums[a]
            target = -nums[a]

            # Since array is sorted, iterate through thre remaining subarray where left_ptr is at index a + 1
            left_ptr, right_ptr =  a + 1, len(nums) - 1

            # SOLVE TWO-SUM HERE: HASHMAP OR TWO POINTERS
            # WE ARE GOING FOR O(1) SPACE WOOO -> TWO POINTERS CAUSE WE SORTED IT

            # Two-Pointer is O(n) Time Complexity and O(1) Space Complexity
            # However since this is done for every n, then O(n * n) = O(n^2)

            # To store the pair
            pairs_b_and_c = []

            # While left pointer hasnt passed the right pointer
            while left_ptr < right_ptr:

                # Calculate the sum of b and c
                sum_of_b_and_c = nums[left_ptr] + nums[right_ptr]

                # If b + c = -a
                if sum_of_b_and_c == target:

                    # Append the pair [b, c]
                    pairs_b_and_c.append([nums[left_ptr], nums[right_ptr]])

                    # Increment the left pointer
                    left_ptr += 1

                    # While the element at the left pointer index is the same as the previous, keep moving the left pointer right
                    while left_ptr < right_ptr and nums[left_ptr] == nums[left_ptr - 1]:

                        left_ptr += 1

                # If b + c < -a, move the left pointer right (b)
                elif sum_of_b_and_c < target:

                    left_ptr += 1

                # If b + c > -a, move the right pointer left (b)
                else:

                    right_ptr -= 1

            # For each pair in the pairs found
            for pair in pairs_b_and_c:

                # Append the triplets such that a and the b + c pair
                triplets.append([nums[a]] + pair)

        # O(nlogn + n^2) = O(n^2) for Time Complexity where n is the length of the array
        # O(n + n) = O(n) space complexity given Python's sort and for the list of pairs
        return triplets