class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams_map = {}

        for word in strs:

            sorted_str = "".join(sorted(word))
            if sorted_str in anagrams_map.keys():
                anagrams_map[sorted_str].append(word)
            else:
                anagrams_map[sorted_str]=[word]
        

        return list(anagrams_map.values())
