class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_list = {}
        for s in strs:
            counts = [0] * 26
            
            for char in s:
                counts[ord(char) - ord('a')] += 1
            
            map_list.setdefault(tuple(counts),[]).append(s)

        result = [p for p in map_list.values()]

        return result
            
            
