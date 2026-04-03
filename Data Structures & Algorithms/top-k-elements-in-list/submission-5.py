from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1
        n = len(nums)

        bucket = [[] for i in range(n + 1)]
        print(bucket)

        for num, freq in freq_map.items():
            bucket[freq].append(num)
        
        res = []

        while k:
            for i in range(len(bucket) - 1, 0, -1):
                if bucket[i] and k:
                    for b in bucket[i]:
                        res.append(b)
                        k -= 1
        
        return res
                    


        