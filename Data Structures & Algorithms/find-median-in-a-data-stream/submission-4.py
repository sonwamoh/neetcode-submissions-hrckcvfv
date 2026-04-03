import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # max heap (using new heapq max functions)
        self.large = []  # min heap

    def addNum(self, num: int) -> None:

        # Decide where to push
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush_max(self.small, num)   # ✔️ valid in Python 3.13+

        # Rebalance heaps
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop_max(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush_max(self.small, val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0]   # ✔️ root of max heap
        elif len(self.large) > len(self.small):
            return self.large[0]   # ✔️ root of min heap
        else:
            return (self.small[0] + self.large[0]) / 2
