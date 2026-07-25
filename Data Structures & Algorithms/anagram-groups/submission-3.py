class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []

        hashmap = {}

        for s in strs:
            count = [0] * 26

            for w in s:
                count[ord(w) - ord("a")] += 1

            key = ""

            for num in count:
                key += '#' + str(num)

            if key not in hashmap:
                hashmap[key] = []

            hashmap[key].append(s)

        return list(hashmap.values())
        
