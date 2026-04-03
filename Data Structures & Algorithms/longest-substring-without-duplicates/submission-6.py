class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {} # store last idx of each char
        left = 0
        n = len(s)
        max_len = 0

        for right in range(n):
            if s[right] in hashmap:
                left = max(hashmap[s[right]] + 1, left)
            
            hashmap[s[right]] = right # updating the last idx
            max_len = max(max_len, right - left + 1)

        return max_len
            

        