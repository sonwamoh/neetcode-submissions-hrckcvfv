from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStrToAnagram = defaultdict(list)

        for word in strs:
            sorted_strs = tuple(sorted(word))
            sortedStrToAnagram[sorted_strs].append(word)

        return list(sortedStrToAnagram.values())

        
        