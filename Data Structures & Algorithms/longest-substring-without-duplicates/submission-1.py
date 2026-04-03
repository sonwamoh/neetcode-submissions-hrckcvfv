from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
            1. hashmap to track ch count in window
            2. while loop to mantain unique ch's in window
            3. track len of longest substr with unique ch
            TC: O(n), one pass
            SC: O(n), suppose we hv all same ch's in the list
        """
        window = defaultdict(int)
        maxLen = 0
        left = 0

        for right in range(len(s)):
            # Also be careful, check for s[right] not right, otherwise, ch = s[right]
            window[s[right]] += 1
            # don't use if statement here
            while window[s[right]] > 1:
                window[s[left]] -= 1
                left += 1
            
            maxLen = max(maxLen, right - left + 1)
        
        return maxLen
            

            
        