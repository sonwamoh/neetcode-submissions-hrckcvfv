class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        n = len(nums)
        bucket = [[] for i in range(n + 1)]

        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1
        
        for num, freq in freq_map.items():
            bucket[freq].append(num)

        res = []
        
        for i in range(len(nums), -1, -1):
            if bucket[i]:
                for num in bucket[i]:
                    res.append(num)
                    if len(res) == k:
                        return res
        
        return []


        