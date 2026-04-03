class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_window = set()
        left = 0
        n = len(s)
        max_len = 0

        for right in range(n):
            while s[right] in unique_window:
                unique_window.remove(s[left])
                left += 1

            max_len = max(max_len, right - left + 1)
            unique_window.add(s[right])
        
        return max_len
            

        