from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # This list will store all of our valid triplets
        result = []

        # Sort the numbers first.
        # Example: [3, -1, 0, 2, -2] -> [-2, -1, 0, 2, 3]
        #
        # Sorting allows us to use the two-pointer technique.
        nums.sort()

        # i represents the first number in our three-number combination
        for i, num in enumerate(nums):

            # If the current number is the same as the previous number,
            # skip it so we don't create duplicate triplets.
            #
            # i > 0 makes sure there actually IS a previous number.
            if i > 0 and num == nums[i - 1]:
                continue

            # The left pointer starts immediately after i
            left = i + 1

            # The right pointer starts at the end of the array
            right = len(nums) - 1

            # Keep moving the pointers until they meet
            while left < right:

                # Add the three numbers together
                three_sum = num + nums[left] + nums[right]

                # If the sum is too large,
                # move the right pointer to a smaller number
                if three_sum > 0:
                    right -= 1

                # If the sum is too small,
                # move the left pointer to a larger number
                elif three_sum < 0:
                    left += 1

                # If the sum is exactly 0,
                # we found a valid triplet!
                else:
                    result.append([num, nums[left], nums[right]])

                    # Move the left pointer forward
                    left += 1

                    # Skip duplicate numbers on the left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        # Return all of the triplets we found
        return result



            
        