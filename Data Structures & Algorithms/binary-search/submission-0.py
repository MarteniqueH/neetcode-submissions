class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #set left at first index 0 
        left = 0 
        #Set right to last position in the array 
        right = len(nums) - 1

        #left position needs to be less than or at the same point as the right not past it 
        while left <= right: 
            #mid point location found by adding the left index with the right index and determining the middle 
            midPoint = (left + right) // 2 

            #if the value of the current midpoint is greater than the target the midpoint needs to move to a smaller value 

            if nums[midPoint] > target:
                right = midPoint - 1
            #if the midpoint value is smaller than the target value the midpoint needs to move to a larger value 
            elif nums[midPoint] < target:
                left = midPoint + 1

            else:
                return midPoint 

        return -1
                

        