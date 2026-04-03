
from heapq import heappush, heappop

class Solution:
    """
        1. Add coor w/ distances to min heap
        2. pop k coor and add it to res
        TC: O(n), iterating through all coordinates
        SC: O(n), minHeap 
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for cord in points:
            heappush(minHeap, (cord[0] ** 2 + cord[1] ** 2, cord))
        
        res = []
        for _ in range(k):
            _, cord = heappop(minHeap)
            res.append(cord)
        
        return res
    

        