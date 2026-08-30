class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(numbers):
            i += 1
            needed = target - num

            if needed in seen:
                return [seen[needed], i]


            seen[num] = i 
        