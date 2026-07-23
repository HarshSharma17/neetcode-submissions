class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}  # regular dictionary
        
        for word in strs:
            # Sort the word
            sorted_word = ''.join(sorted(word))
            
            # If key exists, append; else create new list
            if sorted_word in hashmap:
                hashmap[sorted_word].append(word)
            else:
                hashmap[sorted_word] = [word]
        
        # Return the grouped lists
        return list(hashmap.values())