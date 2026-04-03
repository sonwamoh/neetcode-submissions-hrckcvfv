class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        L, count = 0, {}
        max_len = 0
        max_freq = 0

        for R in range(len(s)):

            count[s[R]] = count.get(s[R], 0) + 1

            max_freq = max(max_freq, count[s[R]])

            if (R - L + 1) - max_freq > k:
                count[s[L]] -= 1
                L += 1
            
            max_len = max(max_len, R - L + 1)
        
        return max_len
            

        