class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        non_overlapping_intervals = [intervals[0]]

        for start, end in intervals[1:]:
            prev_start = non_overlapping_intervals[-1][0]
            prev_end = non_overlapping_intervals[-1][1]

            if prev_end >= start:
                non_overlapping_intervals[-1][1] = max(prev_end, end)
            else:
                non_overlapping_intervals.append([start, end])
        
        return non_overlapping_intervals

                 


        