from typing import List, Dict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in freq_map.items():
            bucket[freq].append(num)
        
        res = []

        for freq in range(len(nums), -1, -1):
            if bucket[freq]:
                for num in bucket[freq]:
                    if len(res) < k:
                        res.append(num)
        return res

                

        
        