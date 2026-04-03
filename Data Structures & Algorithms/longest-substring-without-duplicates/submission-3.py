from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # window will be tracked by left & right pointers
        left = 0
        last_occured = defaultdict(int) # key: ch, val: last idx it occured  # SC: O(N)
        max_len = 0
        n = len(s)

        for right in range(n): #T O(n)
            ch = s[right]

            if ch in last_occured and left <= last_occured[ch]:
                left = last_occured[ch] + 1
            
            last_occured[ch] = right
            max_len = max(max_len, right - left + 1)

        return max_len



            

        