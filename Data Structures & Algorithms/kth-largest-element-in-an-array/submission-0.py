from heapq import heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
            1. make sure we iterate over unique elements in list
            2. create minHeap, store elements in sorted order
            3. then return the topmost elements of the heap
        """
        minHeap = []

        # Trying to mantain the size of the Heap
        for n in nums:
            heappush(minHeap, n)
            if len(minHeap) > k:
                heappop(minHeap)
        
        return minHeap[0]



        