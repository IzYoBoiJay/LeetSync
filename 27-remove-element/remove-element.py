class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        elems_not_val = 0

        for i in range(len(nums)):

            if nums[i] == val:

                continue

            else:

                nums[elems_not_val] = nums[i]
                elems_not_val += 1

        return elems_not_val