class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        max_len = 0
        window = {}

        for R in range(len(s)):
            if s[R] in window:
                L = max(window[s[R]] + 1, L)

            window[s[R]] = R
            max_len = max(max_len, R - L + 1)
        
        return max_len

            
        