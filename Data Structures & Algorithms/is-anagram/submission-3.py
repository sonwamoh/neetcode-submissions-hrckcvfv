class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_freq = [0] * 26

        for ch in s:
            char_freq[ord(ch) - ord('a')] += 1
        
        for ch in t:
            char_freq[ord(ch) - ord('a')] -= 1
        
        for freq in char_freq:
            if freq != 0:
                return False
        
        return True
        