class Solution(object):
    def threeSum(self, nums):
        nums.sort()

        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 

            if nums[i] > 0:
                break 

            left = i + 1 
            right = len(nums) - 1

            while left < right: 

            #I want to see what the current toal is at 

                total = nums[i] + nums[left] + nums[right]

            #what happens if the nums total is bigger 

                if total > 0:
                    right -= 1 

                elif total < 0:
                    left += 1

                else:
                    result.append([nums[i],nums[left],nums[right] ])

                    left += 1 
                    right -= 1


                    while left < right and nums[left] == nums[left-1]:
                        left+= 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1


        return result 

