class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        given: 
            - int array = nums
        return: 
            - true = values appear more than once
            -False = distinct value 
        """

        seen = set()
        

        for num in nums:
            if num in seen:
                return True 


            seen.add(num)

        return False 