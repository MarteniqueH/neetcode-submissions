class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        sorted_num = sorted(count.items(), key = lambda x: x[1], reverse=True)

        result = []
        for i in range(k):
            result.append(sorted_num[i][0])

        return result


