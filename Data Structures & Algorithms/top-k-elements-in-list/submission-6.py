from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1
        
        min_heap = [] #[(freq, key)]
        # so heap sort its 1st by freq and then by key
        
        for n in freq_map.keys():
            heapq.heappush(min_heap, (freq_map[n], n))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        res = []

        for i in range(k):
            res.append(min_heap[i][1])
            
        return res

        

        
                    


        