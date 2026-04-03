from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ch_count = [0] * 26
        
        for ch in s:
            ch_count[ord(ch) - ord('a')] += 1
        
        for ch in t:
            ch_count[ord(ch) - ord('a')] -= 1
        
        for count in ch_count:
            if count != 0:
                return False
        
        return True
        
        